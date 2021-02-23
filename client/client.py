# Echo client program
import socket
import json


HOST = 'localhost'
PORT = 40000

def connection(payload, host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        payload_str = str.encode(json.dumps(payload))
        client.sendall(payload_str)

        response = client.recv(1024)
    return json.loads(response.decode())
