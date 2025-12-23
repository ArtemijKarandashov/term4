import grpc
from fastapi import FastAPI

import glossary_pb2
import glossary_pb2_grpc

app = FastAPI()

channel = grpc.insecure_channel("localhost:50051")
stub = glossary_pb2_grpc.GlossaryServiceStub(channel)


@app.get("/terms")
def list_terms():
    response = stub.ListTerms(glossary_pb2.Empty())
    return [{"name": t.name, "definition": t.definition} for t in response.terms]


@app.get("/terms/{name}")
def get_term(name: str):
    response = stub.GetTerm(glossary_pb2.GetTermRequest(name=name))
    return {"name": response.name, "definition": response.definition}


@app.post("/terms")
def add_term(name: str, definition: str):
    response = stub.AddTerm(
        glossary_pb2.AddTermRequest(name=name, definition=definition)
    )
    return {"name": response.name, "definition": response.definition}
