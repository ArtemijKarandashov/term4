# gRPC + Web API

## Build & Run
docker build -t glossary-service .
docker run -p 8000:8000 -p 50051:50051 glossary-service

## API
GET /terms
GET /terms/{name}
POST /terms?name=...&definition=...
