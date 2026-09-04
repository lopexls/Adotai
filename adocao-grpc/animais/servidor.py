import grpc

from concurrent import futures

import adocao_pb2
import adocao_pb2_grpc


class AnimalService(adocao_pb2_grpc.AnimalServiceServicer):

    animais = [
        {
            "id": 1,
            "nome": "Thor",
            "especie": "Cachorro",
            "idade": 3,
            "disponivel": True
        },
        {
            "id": 2,
            "nome": "Mel",
            "especie": "Gato",
            "idade": 2,
            "disponivel": True
        },
        {
            "id": 3,
            "nome": "Bob",
            "especie": "Cachorro",
            "idade": 5,
            "disponivel": False
        }
    ]

    def ListarAnimaisDisponiveis(self, request, context):

        resposta = adocao_pb2.ListaAnimaisResponse()

        for animal in self.animais:

            if animal["disponivel"]:

                resposta.animais.add(
                    id=animal["id"],
                    nome=animal["nome"],
                    especie=animal["especie"],
                    idade=animal["idade"]
                )

        return resposta

    def VerificarAnimal(self, request, context):

        for animal in self.animais:

            if animal["id"] == request.animal_id:

                return adocao_pb2.VerificarAnimalResponse(
                    animal=adocao_pb2.Animal(
                        id=animal["id"],
                        nome=animal["nome"],
                        especie=animal["especie"],
                        idade=animal["idade"]
                    ),
                    disponivel=animal["disponivel"]
                )

        return adocao_pb2.VerificarAnimalResponse(
            disponivel=False
        )

    def SolicitarAdocao(self, request, context):

        for animal in self.animais:

            if animal["id"] == request.animal_id:

                if not animal["disponivel"]:

                    return adocao_pb2.SolicitarAdocaoResponse(
                        sucesso=False,
                        mensagem="Animal não está disponível para adoção."
                    )

                animal["disponivel"] = False

                print(
                    f"Adoção solicitada: "
                    f"{request.nome_adotante} adotou {animal['nome']}"
                )

                return adocao_pb2.SolicitarAdocaoResponse(
                    sucesso=True,
                    mensagem=f"Adoção de {animal['nome']} realizada com sucesso!"
                )

        return adocao_pb2.SolicitarAdocaoResponse(
            sucesso=False,
            mensagem="Animal não encontrado."
        )


def main():

    servidor = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    adocao_pb2_grpc.add_AnimalServiceServicer_to_server(
        AnimalService(),
        servidor
    )

    servidor.add_insecure_port("[::]:9090")

    servidor.start()

    print("Microsserviço de Animais ouvindo na porta 9090")

    servidor.wait_for_termination()


if __name__ == "__main__":
    main()