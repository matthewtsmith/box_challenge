package main

import (
	"net/http"
	"net"
	"google.golang.org/grpc"
	"io/ioutil"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"os"
	"golang.org/x/net/context"
	"log"
	"github.com/gedex/bp3d"
	"fmt"
)

type server struct {

}

func (server) Pack(ctx context.Context, req *PackRequest) (*PackResponse, error) {
	p := bp3d.NewPacker()

	for _, box := range req.Boxes {
		p.AddBin(bp3d.NewBin(box.Id, box.Width, box.Height, box.Length	, box.MaxWeight))
	}
	for _, prod := range req.Items {
		for i := int32(0); i < prod.Qty; i++ {
			p.AddItem(bp3d.NewItem(prod.Id, prod.Width, prod.Height, prod.Length, prod.Weight))
		}
	}

	if err := p.Pack(); err != nil {
		return nil, err
	}
	resp := &PackResponse{}
	for _, bin := range p.Bins {
		if len(bin.Items) == 0 {continue}
		packedBox := PackedBox{
			Box:   &Box{
				Id:        bin.Name,
				Length:    bin.Depth,
				Width:     bin.Width,
				Height:    bin.Height,
				MaxWeight: bin.MaxWeight,
			},
		}
		var products []*Item
		for _, item := range bin.Items {
			products = append(products, &Item{
				Id:       item.Name,
				Length:   item.Depth,
				Width:    item.Width,
				Height:   item.Height,
				Weight:   0,
			})
		}
		packedBox.Items = products
		resp.Boxes = append(resp.Boxes, &packedBox)
	}
	displayPacked(p.Bins)
	return resp, nil
}

func displayPacked(bins []*bp3d.Bin) {
	for _, b := range bins {
		fmt.Println(b)
		fmt.Println(" packed items:")
		for _, i := range b.Items {
			fmt.Println("  ", i)
		}
	}
}

func startGRPC(port string) error {
	lis, err := net.Listen("tcp", ":"+port)
	if err != nil {
		return err
	}
	s := grpc.NewServer()
	RegisterPackerServer(s,&server{})
	return s.Serve(lis)
}

func cors(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		Set(w, AccessControl{
			Origin:         "*",
			AllowedMethods: []string{"GET", "HEAD", "OPTIONS", "POST", "PUT", "DELETE", "PATCH"},
		})
		next.ServeHTTP(w, r)
	})
}

func startHTTP(httpPort, grpcPort string) error {
	schema, err := ioutil.ReadFile("pack.swagger.json")
	if err != nil {
		return err
	}
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	gwmux := runtime.NewServeMux()
	opts := []grpc.DialOption{grpc.WithInsecure()}
	if err := RegisterPackerHandlerFromEndpoint(ctx, gwmux, "127.0.0.1:"+grpcPort, opts); err != nil {
		return err
	}

	mux := http.NewServeMux()
	mux.HandleFunc("/v1/packer/swagger", func(w http.ResponseWriter, r *http.Request) {
		Set(w, ContentType("application/json"))
		w.WriteHeader(http.StatusOK)
		w.Write(schema)
	})
	mux.Handle("/v1/", gwmux)
	mux.Handle("/", http.FileServer(http.Dir("swagger-ui")))

	http.ListenAndServe(":"+httpPort, cors(mux))
	return nil
}

func main() {
	errors := make(chan error)

	httpPort := os.Getenv("PORT")
	if httpPort == "" {
		httpPort = "8080"
	}

	grpcPort := os.Getenv("GRPC_PORT")
	if grpcPort == "" {
		grpcPort = "50080"
	}

	if grpcPort == httpPort {
		panic("Can't listen on the same port")
	}

	go func() {
		errors <- startGRPC(grpcPort)
	}()

	go func() {
		errors <- startHTTP(httpPort, grpcPort)
	}()

	for err := range errors {
		log.Fatal(err)
		return
	}
}