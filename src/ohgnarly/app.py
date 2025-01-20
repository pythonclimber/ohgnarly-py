from urllib.request import Request

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import PlainTextResponse, FileResponse


async def root(_):
    return PlainTextResponse('Hello, world!', status_code=200)


async def favicon(_):
    return FileResponse("static/favicon.ico")



app = Starlette(
    debug=False,
    routes=[
        Route("/", endpoint=root),
        Route("/favicon.ico", endpoint=favicon),
        Mount("/static", StaticFiles(directory="src/ohgnarly/static"), name="static"),
    ]
)