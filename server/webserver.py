import asyncio
import websockets

async def hello(websocket, path):
    while True:
        request = await websocket.recv()
        print(f"< {request}")

        await websocket.send(request)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()