import asyncio
import requests
from aiohttp import web

print("privet")



async def hello1(request1):
    await asyncio.sleep(5)
    peername =  request1.transport.get_extra_info('peername')

    if peername:
        host, port = peername
    else:
        print("request is empty")
    return web.json_response(dict(response="Hello, world1", ip=host, port=port))

async def hello2(request):
    await asyncio.sleep(5)
    peername =  request.transport.get_extra_info('peername')
    if peername:
        host, port = peername
    else:
        print("request is empty")
    return web.json_response(dict(response="Hello, world2",ip2=host, port2=port))

def make_app():
    app = web.Application()
    app.add_routes([web.get('/1/', hello1), web.get('/2/', hello2)])
    return app


if __name__ == "__main__":
    app = make_app()
    web.run_app(app)