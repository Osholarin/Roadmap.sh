from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from convert import convert_length, convert_weight, convert_temperature

# initialize the fastapi app
app = FastAPI()

# loading the templates and styling files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def return_length_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.get("/weight", response_class=HTMLResponse)
def return_weight_form(request: Request):
    return templates.TemplateResponse("weight.html", {"request": request, "result": None})

@app.get("/temperature", response_class=HTMLResponse)
def return_temperature_form(request: Request):
    return templates.TemplateResponse("temperature.html", {"request": request, "result": None})

@app.post("/length", response_class=HTMLResponse)
async def get_length(
    request: Request, 
    entry: float = Form(...),
    unit: str = Form(...), 
    new_unit: str = Form(...)):

    result = None
    error = None
    
    try:
        result = convert_length(entry, unit, new_unit)
        return templates.TemplateResponse("index.html", {"request": request, "result": result})
    except ValueError as e:
        error = str(e)
        return templates.TemplateResponse("index.html", {"request": request, "result": result, "error": error})
    
@app.post("/weight", response_class=HTMLResponse)
async def get_weight(
    request: Request, 
    entry: float = Form(...),
    unit: str = Form(...), 
    new_unit: str = Form(...)):

    result = None
    error = None

    try:
        result = convert_weight(entry, unit, new_unit)
        return templates.TemplateResponse("weight.html", {"request": request, "result": result})
    except ValueError as e:
        error = str(e)

        return templates.TemplateResponse("weight.html", {"request": request, "result": result, "error": error})

@app.post("/temperature", response_class=HTMLResponse)
async def get_temperature(
    request: Request, 
    entry: float = Form(...),
    unit: str = Form(...), 
    new_unit: str = Form(...)):

    result = None
    error = None

    try:
        result = convert_temperature(entry, unit, new_unit)
        return templates.TemplateResponse("temperature.html", {"request": request, "result": result})
    except ValueError as e:
        error = str(e)

        return templates.TemplateResponse("temperature.html", {"request": request, "result": result, "error": error})