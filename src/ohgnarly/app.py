from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/ohgnarly/templates")


async def root(request: Request):
    return templates.TemplateResponse(
        request,
        "layout.html",
        context={"request": request},
    )


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