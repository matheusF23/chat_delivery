from client import connection


while True:
    print("Seja bem vindo ao Chat delivery\n")
    res = int(input("Gostaria de realizar um pedido?\n1. Sim\n2. Não\n"))
    if res == 2:
        break
    print("Escolha seu pedido")
    payload = {
        "method": "list",
        "body": None
    }

    response = connection(payload)
    for i in response:
        print(i, response[i])

print("Volte sempre!")