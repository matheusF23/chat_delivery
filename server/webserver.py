import asyncio
import websockets
import json


ORDERS = {}

OPTIONS = [
    "tradicional", "smash", "vegano",
    "calabresa", "frango", "mussarela",
    "carne", "queijo", "pizza",
    "guaraná", "jesus", "coca"
]

PRICES = [
    17.00, 15.00, 18.00,
    27.00, 30.00, 25.00,
    05.00, 05.00, 05.00,
    05.00, 05.00, 05.00 
]

INITIAL_MESSAGE = """
    Olá, para visualizar o menu envie: 'menu'.</br>
    Para adicionar opções ao pedido envie:
    'add opção quantidade'.</br>
    Por exemplo: add guaraná 1</br>
    Para visualisar seu pedido envie:
    'pedido'</br>
    Para finalizar o pedido envie:
    'finalizar'
"""

MENU = """
    <h2> Hamburguers </h2>
    Tradicional: R$ 17,00</br>
    Smash: R$ 15,00</br>
    Vegano: R$ 18,00</br>
    <h2> Pizzas </h2>
    Calabresa: R$ 27,00</br>
    Frango: R$ 30,00</br>
    Mussarela: R$ 25,00</br>
    <h2> Pastéis </h2>
    Carne: R$ 05,00</br>
    Queijo: R$ 05,00</br>
    Pizza: R$ 05,00</br>
    <h2> Refrigerante (Latinha) </h2>
    Guaraná: R$ 05,00</br>
    Jesus: R$ 05,00</br>
    Coca: R$ 05,00</br>
"""

async def list_menu(websocket):
    await websocket.send(MENU)

async def add_order(websocket, order, qty):
    try:
        if websocket not in ORDERS:
            ORDERS[websocket] = []
        for i, opt in enumerate(OPTIONS):
            if order == opt:
                value_option = PRICES[i]*int(qty)
                ORDERS[websocket].append((order, int(qty), value_option))
    except:
        await websocket.send("Algo de errado não está certo. Tente novamente")

async def show_order(websocket):
    try:
        response = ""
        total = 0
        for order in ORDERS[websocket]:
            response += f"<strong>{order[1]} '{order[0]}'</strong> -> R$ {order[2]}0</br>"
            total += order[2]
        response += f"<strong>Total: R$ {total}0</strong>"
        await websocket.send(response)
    except:
        await websocket.send("Nada ainda...")
    

async def chat_server(websocket, path):
    try:
        await websocket.send(INITIAL_MESSAGE)

        async for request in websocket:
            message = request.split(" ")
            if message[0] == "menu":
                await list_menu(websocket)
            elif message[0] == "add":
                if len(message) >= 3:
                    if message[1] in OPTIONS:
                        await add_order(websocket, message[1], message[2])
                    else:
                        await websocket.send("Opção ou quantidade inválida")
                else:
                    await websocket.send("Ops, é preciso escolher uma opção e sua quantidade")
            elif message[0] == 'pedido':
                await show_order(websocket)
            elif message[0] == 'finalizar':
                await websocket.send('Pedido finalizado. Aguarde que um dia chega.')
                await websocket.close()
            else:
                await websocket.send("Olá, deseja realizar um pedido? As orientações estão acima")
    except:
        pass

start_server = websockets.serve(chat_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
