import asyncio

from aiohttp import web

print("privet")

async def hello1(request):
    await asyncio.sleep(5)
    print(type(request))
    print(request)
    return web.json_response(dict(response="Hello, world1"))

async def hello2(request):
    await asyncio.sleep(5)
    print(type(request))
    print(request)
    return web.json_response(dict(response="Hello, world2"))

def make_app():
    app = web.Application()
    app.add_routes([web.get('/1/', hello1), web.get('/2/', hello2)])
    return app


if __name__ == "__main__":
    app = make_app()
    web.run_app(app)