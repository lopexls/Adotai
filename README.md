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

Em Linux (VM Google Cloud):  

**CONFIGURAÇÃO INICIAL**  

0.1- Instale o pip (execute os dois abaixo):  
sudo apt update  
sudo apt install python3-pip  

0.2- Instale o ambiente virtual do python (venv):  
sudo apt install python3-full  

0.3- Git clone este repositório e em seguida acesse a pasta SD2026 -> adocao-grpc:  
git clone https://github.com/Rodrigo-Yuji/SD2026.gls  

0.4- Crie o ambiente virtual e acesse-o:  
python3 -m venv venv  
source venv/bin/activate  

0.5- Instale o GRPC:  
pip install grpcio grpcio-tools  

**INICIALIZAÇÃO DO SISTEMA (EXECUTAR SEMPRE QUE FECHAR A MÁQUINA OU EM NOVA INSTÂNCIA)**  

1- Acesse a pasta adocao-grpc e abra o ambiente virtual com:  
cd ~/adocao-grpc  
source venv/bin/activate  

1.1- Compilar .proto:  
python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/adocao.proto  

2- Inicie os servidores/cliente:  
para rodar servidor doação  
python -m animais.servidor  

para rodar servidor animais  
python -m adocao.servidor  

para rodar cliente:  
python -m adocao.cliente  
