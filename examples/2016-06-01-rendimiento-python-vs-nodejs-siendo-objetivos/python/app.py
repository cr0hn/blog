import asyncio

from aiohttp import web


@asyncio.coroutine
def home(request):
    return web.Response(body=b"""<!DOCTYPE html>
<html lang="es">
<head>
	<title>Hello world!</title>
</head>
<body>
<p>P&aactue;gina de prueba</p>
</body>
</html>""")


@asyncio.coroutine
def json_path(request):
    return web.json_response({"test": 1, "data": "hello world" })


def main():
    app = web.Application()
    app.router.add_route('GET', '/', home)
    app.router.add_route('GET', '/json', json_path)

    web.run_app(app, port=8081, backlog=5000)

if __name__ == '__main__':
    main()
