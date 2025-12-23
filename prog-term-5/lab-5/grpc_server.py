import grpc
from concurrent import futures

import glossary_pb2
import glossary_pb2_grpc


class GlossaryService(glossary_pb2_grpc.GlossaryServiceServicer):
    def __init__(self):
        self.terms = {
            "Python": "Интерпретируемый язык программирования",
            "gRPC": "RPC-фреймворк от Google",
            "Protobuf": "Формат сериализации данных"
        }

    def GetTerm(self, request, context):
        definition = self.terms.get(request.name, "")
        return glossary_pb2.TermResponse(
            name=request.name,
            definition=definition
        )

    def ListTerms(self, request, context):
        return glossary_pb2.TermsListResponse(
            terms=[
                glossary_pb2.TermResponse(name=k, definition=v)
                for k, v in self.terms.items()
            ]
        )

    def AddTerm(self, request, context):
        self.terms[request.name] = request.definition
        return glossary_pb2.TermResponse(
            name=request.name,
            definition=request.definition
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(
        GlossaryService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
