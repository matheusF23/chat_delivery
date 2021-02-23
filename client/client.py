import socket


HOST = 'localhost'
PORT = 40000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(str.encode('Hello socket'))

data = client.recv(1024)

print(f'Mensagem ecoada: {data.decode()}')
