from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
import string

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate_password(
    request: Request,
    length: int = Form(12),
    uppercase: bool = Form(),
    digits: bool = Form(False),
    symbols: bool = Form(False)
):

    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    try:
        length = int(length)

    except ValueError as e:
        return templates.TemplateResponse("form.html", {"request": request, "error": str(e)})

    password = "".join(random.choice(characters) for _ in range(length))
    return templates.TemplateResponse("form.html", {"request": request, "password": password})
