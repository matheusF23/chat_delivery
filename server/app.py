import json

def list_menu(conn):
    menu = {
        "Hamburguer": 15,
        "Batata": 8,
        "Refri": 5,
        "Salada": 14
    }
    payload = str.encode(json.dumps(menu))
    conn.sendall(payload)
