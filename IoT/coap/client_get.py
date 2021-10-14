import logging
import asyncio
import time
from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    await asyncio.sleep(2)
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://10.0.0.3/other/separate')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    while True:    
        asyncio.get_event_loop().run_until_complete(main())
