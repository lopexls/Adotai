Em Windows:

1- Instalar GRPC, no cmd, execute:
pip install grpcio grpcio-tools

2- Git clone este repositório
git clone https://github.com/Rodrigo-Yuji/SD2026.git

Caso haja alteração no .proto, deve-se sobrescrever os arquivos (compilar)
adocao_pb2.py
adocao_pb2_grpc.py
com o seguinte comando no CMD (dentro da pasta adocao-grpc)
python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/adocao.proto


Para executar:
Acesse o CMD (dentro da pasta adocao-grpc) em 3 terminais diferentes:
para rodar servidor doação
python -m animais.servidor

para rodar servidor animais
python -m adocao.servidor

para rodar cliente:
python -m adocao.cliente
