
import json
from urllib.request import Request, urlopen

# Dirección local de nuestra API.
# Después la cambiaremos por la dirección pública de Render.
URL_BASE = "http://127.0.0.1:8000"

def probar_api():
    print("=== PRUEBAS DE MI API ===")

    # Prueba 1: Inicio
    with urlopen(f"{URL_BASE}/") as respuesta:
        print("\nPRUEBA 1 - GET /")
        print("Código:", respuesta.status)
        print("Respuesta:", respuesta.read().decode("utf-8"))

    # Prueba 2: Saludo
    with urlopen(f"{URL_BASE}/saludo/Adriana") as respuesta:
        print("\nPRUEBA 2 - GET /saludo/Adriana")
        print("Código:", respuesta.status)
        print("Respuesta:", respuesta.read().decode("utf-8"))

    # Prueba 3: Crear artículo
    datos = {
        "nombre": "Laptop",
        "precio": 15000
    }

    solicitud = Request(
        f"{URL_BASE}/items/",
        data=json.dumps(datos).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urlopen(solicitud) as respuesta:
        print("\nPRUEBA 3 - POST /items/")
        print("Código:", respuesta.status)
        print("Respuesta:", respuesta.read().decode("utf-8"))

    print("\n¡Todas las pruebas finalizaron correctamente!")

if __name__ == "__main__":
    probar_api()
