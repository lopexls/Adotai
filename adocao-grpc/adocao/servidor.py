import grpc

from concurrent import futures

import adocao_pb2
import adocao_pb2_grpc


class AdocaoService(adocao_pb2_grpc.AdocaoServiceServicer):

    def __init__(self):

        # Conecta no Microsserviço de Animais
        canal = grpc.insecure_channel("localhost:9090")

        self.animal_stub = adocao_pb2_grpc.AnimalServiceStub(canal)


    def SolicitarAdocao(self, request, context):

        print()
        print("=== NOVA SOLICITAÇÃO DE ADOÇÃO ===")
        print(f"Adotante: {request.nome_adotante}")
        print(f"Animal solicitado: {request.animal_id}")

        # Primeiro verifica o animal
        print("→ Consultando Microsserviço de Animais...")

        resposta_animal = self.animal_stub.VerificarAnimal(
            adocao_pb2.VerificarAnimalRequest(
                animal_id=request.animal_id
            )
        )

        # Verifica se o animal existe
        if resposta_animal.animal.id == 0:

            print("← Animal não encontrado.")
            print("=== FIM DA SOLICITAÇÃO ===")
            print()

            return adocao_pb2.SolicitarAdocaoResponse(
                sucesso=False,
                mensagem="Animal não encontrado."
            )

        print(
            f"← Animal encontrado: "
            f"{resposta_animal.animal.nome}"
        )

        # Verifica se está disponível
        if not resposta_animal.disponivel:

            print("← Animal está indisponível.")
            print("=== FIM DA SOLICITAÇÃO ===")
            print()

            return adocao_pb2.SolicitarAdocaoResponse(
                sucesso=False,
                mensagem="Animal não está disponível."
            )

        print("← Animal está disponível.")

        # Solicita a adoção ao Microsserviço de Animais
        print(
            "→ Enviando solicitação de adoção "
            "para Microsserviço de Animais..."
        )

        resposta_adocao = self.animal_stub.SolicitarAdocao(
            adocao_pb2.SolicitarAdocaoRequest(
                animal_id=request.animal_id,
                nome_adotante=request.nome_adotante
            )
        )

        print(
            f"← Resposta recebida: "
            f"{resposta_adocao.mensagem}"
        )

        print("=== FIM DA SOLICITAÇÃO ===")
        print()

        return resposta_adocao


def main():

    servidor = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    adocao_pb2_grpc.add_AdocaoServiceServicer_to_server(
        AdocaoService(),
        servidor
    )

    servidor.add_insecure_port("[::]:9091")

    servidor.start()

    print("Microsserviço de Adoção ouvindo na porta 9091")

    servidor.wait_for_termination()


if __name__ == "__main__":
    main()