from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

recieved_arguments = []

class Values(BaseModel):
    entry: int
    unit: str
    new_unit: str

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": None})

@app.get("/weight", response_class=HTMLResponse)
def return_form(request: Request):
    return templates.TemplateResponse("weight.html", {"request": request, "data": None})

@app.get("/temperature", response_class=HTMLResponse)
def return_form(request: Request):
    return templates.TemplateResponse("temperature.html", {"request": request, "data": None})

@app.post("/length", response_class=HTMLResponse)
async def get_arguements(
    request: Request, 
    entry: int = Form(...), 
    unit: str = Form(...), 
    new_unit: str = Form(...)):

    data = Values(entry=entry, unit=unit, new_unit=new_unit)
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.post("/weight", response_class=HTMLResponse)
async def get_arguements(
    request: Request, 
    entry: int = Form(...), 
    unit: str = Form(...), 
    new_unit: str = Form(...)):

    data = Values(entry=entry, unit=unit, new_unit=new_unit)
    return templates.TemplateResponse("weight.html", {"request": request, "data": data})

@app.post("/temperature", response_class=HTMLResponse)
async def get_arguements(
    request: Request, 
    entry: int = Form(...), 
    unit: str = Form(...), 
    new_unit: str = Form(...)):

    data = Values(entry=entry, unit=unit, new_unit=new_unit)
    return templates.TemplateResponse("temperature.html", {"request": request, "data": data})