import socket


HOST = 'localhost'
PORT = 40000

# INET - trabalhar com IPv4, SOCK_STREAM - TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))     # Vincula o host e a porta com o socket
server.listen()
print("Aguardando conexão de um cliente")

# Aceita a conexão com o cliente e retorna a conexão e o endereço do cliente
conn, address = server.accept()
print(f"Conectado em {address}")

while True:
    data = conn.recv(1024)  # Recebe os dados do cliente

    if not data:
        print("Fechando a conexão")
        conn.close()    # Finaliza a conexão
        break

    conn.sendall(data)  # Envia dados para o cliente
