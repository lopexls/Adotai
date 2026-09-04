import grpc

import adocao_pb2
import adocao_pb2_grpc


def main():

    with grpc.insecure_channel("localhost:9091") as canal:

        stub = adocao_pb2_grpc.AdocaoServiceStub(canal)

        nome = input("Digite seu nome: ")

        animal_id = int(
            input("Digite o ID do animal que deseja adotar: ")
        )

        resposta = stub.SolicitarAdocao(
            adocao_pb2.SolicitarAdocaoRequest(
                animal_id=animal_id,
                nome_adotante=nome
            )
        )

        print()
        print(resposta.mensagem)


if __name__ == "__main__":
    main()