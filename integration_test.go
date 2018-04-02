package main

import (
	"testing"
	"google.golang.org/grpc"
	"context"
	"encoding/json"
	"strings"
	"fmt"
)

var exampleData = `{
  "items": [
    {
      "id": "SEAL-DRIVE-SHAFT",
      "length": 1.50,
      "width": 1.50,
      "height": 1.50,
      "qty": 11
    },
    {
      "id": "BRUSH A.-PACKAGE-GRAVITY",
      "length": 12.00,
      "width": 4.00,
      "height": 20.00,
      "qty": 1
    },
    {
      "id": "BLADE-SCRAPER-PLASTIC",
      "length": 1.00,
      "width": 0.38,
      "height": 9.75,
      "qty": 5
    }
  ],
  "boxes": [
    {
      "id": "A",
      "length": 12,
      "height": 12,
      "width": 12
    },
    {
      "id": "B",
      "length": 20,
      "height": 20,
      "width": 14
    },
    {
      "id": "C",
      "length": 38,
      "height": 25,
      "width": 15
    },
    {
      "id": "D",
      "length": 60,
      "height": 15,
      "width": 15
    }
  ]
}`

func Test_Pack(t *testing.T) {
	conn, err := grpc.Dial("127.0.0.1:50080", grpc.WithInsecure())
	if err != nil {
		t.Fail()
	}
	defer conn.Close()
	client := NewPackerClient(conn)
	reader := strings.NewReader(exampleData)
	decoder := json.NewDecoder(reader)
	packReq := &PackRequest{}
	err = decoder.Decode(packReq)
	if err != nil {
		t.Error(err)
	}
	resp, err := client.Pack(context.Background(), packReq)
	if err != nil {
		t.Error(err)
		t.FailNow()
	}
	if len(resp.Boxes) == 0 {
		t.Fail()
	}
	for _, b := range resp.Boxes {
		print(fmt.Sprintf("Box %s - %f w x %f h x %f l has:\n", b.Box.Id, b.Box.Width, b.Box.Height, b.Box.Length))
		for _, item := range b.Items {
			println(item.Id)
		}
	}
}
