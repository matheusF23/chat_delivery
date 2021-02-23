# Echo server program
import socket
import json

import app


HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 40000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Aguardando conexão de um cliente")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            data_json = json.loads(data)
            method = data_json["method"]
            payload = data_json["body"]

            if method == "list":
                app.list_menu(conn)
