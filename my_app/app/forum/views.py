import aiohttp_jinja2
from my_app.planets_api import res

# создаем функцию, которая будет отдавать html-файл
@aiohttp_jinja2.template("index.html")
async def index(request):
    return {"results": res}

