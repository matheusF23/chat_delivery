# Chat delivery

Esta aplicação faz uso de websocket com o python para exemplificar uma comunicação cliente servidor.

## Clonar projeto para desenvolvimento
Use o comando para clonar o projeto em seu computador
```
$ git clone git@github.com:matheusF23/chat_delivery.git
```
## Instalar dependências
### Ambiente virtual
Vá para o diretório do projeto
```
$ cd chat_delivery
```
Para instalar o ambiente virtual use os comandos
```
$ pip install virtualenv
$ virtualenv venv -p python
```
Para ativar o ambiente virtual use o comando
- linux `source venv/bin/activate`
- windows `venv\Scripts\activate`
### Instalação das dependências
Para instalar as dependências use o comando
```
$ pip install -r requirements.txt
```

## Execução do projeto
Estando na pasta do projeto execute o arquivo [webserver.py](server/webserver.py)
```
$ python server/webserver.py
```

Abra o arquivo [index.html](client/index.html) no navegador e envie os comandos para o chat.
