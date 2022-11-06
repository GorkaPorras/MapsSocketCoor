import asyncio
import websockets

async_mode = None

async def server(ws:str, path:int):
   
    while True:
        lat=input("lat: ")
        lng=input("lng: ")
        await ws.send('{"lat":'+lat+',"lng":'+lng+'}');
        message = await ws.recv()
        print(f'Map [{message}]')
    
Server = websockets.serve(server, '127.0.0.1', 5001)

asyncio.get_event_loop().run_until_complete(Server)
asyncio.get_event_loop().run_forever()