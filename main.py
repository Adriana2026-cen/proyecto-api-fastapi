
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Mi primera API",
    description="API creada con FastAPI para mi proyecto escolar",
    version="1.0.0"
)

class Item(BaseModel):
    nombre: str
    precio: float

@app.get("/")
def inicio():
    return {
        "mensaje": "¡Mi API está funcionando!",
        "autor": "Adriana Cen"
    }

@app.get("/saludo/{usuario}")
def saludar(usuario: str):
    return {
        "mensaje": f"Hola, {usuario}. ¡Bienvenido a mi API!"
    }

@app.post("/items/")
def crear_item(item: Item):
    return {
        "mensaje": "Artículo recibido correctamente",
        "item": item
    }
