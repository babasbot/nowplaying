import asyncio
import lastfm
import sys
import time
import websockets

async def now_playing(websocket, path):
    last_track = None

    while True:
        current_track = lastfm.now_playing(username) 
        
        if current_track != last_track:
            await websocket.send(f'now playing: {current_track} ♫')

            last_track = current_track

        time.sleep(3)

if __name__ == "__main__":
    username = sys.argv[1]
    server   = websockets.serve(now_playing, 'localhost', 8080)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
