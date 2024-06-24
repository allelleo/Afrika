from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="site/static"), name="static")

templates = Jinja2Templates(directory="site")


@app.get("/")
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app)  # , host="62.109.29.105")
