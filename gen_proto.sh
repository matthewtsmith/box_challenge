#!/usr/bin/env bash
protoc -I/usr/local/include -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis pack.proto --go_out=plugins=grpc:.
protoc -I/usr/local/include -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis --grpc-gateway_out=logtostderr=true:. pack.proto
protoc -I/usr/local/include -I. -I$GOPATH/src -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis --swagger_out=logtostderr=true:. pack.proto
#protoc -I/usr/local/include -I. -I$GOPATH/src -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis --go_out=plugins=grpc+retag:. pack.proto

protoc -I/usr/local/include -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis pack.proto --java_out=.
protoc -I/usr/local/include -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis pack.proto --cpp_out=.
protoc -I/usr/local/include -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis pack.proto --csharp_out=.
protoc -I/usr/local/include -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis pack.proto --python_out=.

#protoc-go-inject-tag -input=./pack.pb.go