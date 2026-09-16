# application-test-suite

Suite de pruebas de API para el servicio de autenticación JWT-cookieParser.
Desacoplada del servicio: dependencias propias, configuración por variables de
entorno, cero imports del código de la aplicación.

## Requisitos
- Python 3.12+
- El servicio bajo prueba corriendo y accesible

## Setup
    python -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Configuración
| Variable   | Default                 | Descripción                  |
|------------|-------------------------|------------------------------|
| `BASE_URL` | `http://localhost:8080` | URL del servicio bajo prueba |
| `TIMEOUT`  | `10`                    | Timeout HTTP en segundos     |

## Correr
    pytest                                  # todo lo del gate
    pytest -m smoke                         # solo camino crítico
    pytest -m "not external and not e2e"    # lo que corre en CI

## Markers
Ver `pytest.ini`. `external` y `e2e` quedan fuera del gate de PR a propósito:
el primero depende de un round-trip real con GitHub OAuth, el segundo necesita
navegador. No es que no corran — corren en otra cadencia.