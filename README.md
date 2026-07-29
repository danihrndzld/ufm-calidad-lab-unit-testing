# Laboratorio: Pruebas Unitarias

**Calidad y Automatización en Ingeniería de Software** — UFM, Semestre 2, 2026
Se introduce en el Módulo 1 (tipos y niveles de prueba, nivel unitario) y se
retoma con más profundidad en el Módulo 3 (`pytest`, TDD, dobles de prueba).

---

## Qué es este laboratorio

Un paquete de Python con siete funciones pequeñas, puras y sin dependencias.
Las funciones ya están escritas; **las pruebas no**. Tu trabajo es escribirlas.

Cada función tiene un docstring que describe exactamente qué debe hacer. Ese
docstring es la **especificación**: es contra él —y no contra el código— que
decides si un resultado es correcto. Léelo antes de escribir cada prueba.

> Dos de las funciones **no cumplen su especificación**. No están marcadas.
> Una suite de pruebas rigurosa las encuentra; una descuidada pasa de largo.
> Encontrarlas es parte de la entrega.

---

## Requisitos previos

Solo necesitas [`uv`](https://docs.astral.sh/uv/), el gestor de proyectos de
Python. Él se encarga del intérprete y de las dependencias.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS con Homebrew
brew install uv
```

Verifica la instalación:

```bash
uv --version
```

No instales Python a mano y no crees el entorno virtual tú: `uv` descarga
Python 3.12 automáticamente la primera vez.

---

## Cómo arrancar

```bash
git clone https://github.com/danihrndzld/ufm-calidad-lab-unit-testing.git
cd ufm-calidad-lab-unit-testing

uv sync          # crea .venv e instala pytest
uv run pytest    # ejecuta la suite
```

En un clon recién hecho debes ver **1 prueba que pasa** (el ejemplo resuelto)
y ninguna que falle. Si eso funciona, ya puedes empezar.

Comandos que vas a usar todo el tiempo:

| Comando | Para qué |
|---|---|
| `uv run pytest` | Corre todas las pruebas |
| `uv run pytest -q` | Salida corta |
| `uv run pytest -v` | Muestra el nombre de cada prueba |
| `uv run pytest tests/test_username.py` | Corre un solo archivo |
| `uv run pytest -k username` | Corre las pruebas cuyo nombre contiene "username" |

---

## Estructura

```
src/lab_unit_testing/
├── validators.py    validate_username
├── text.py          to_upper, to_lower, count_words, is_palindrome
└── numeric.py       is_leap_year, clamp

tests/
├── test_example.py  ← ejemplo resuelto y comentado (no lo borres)
├── test_username.py ← escribe aquí
├── test_text.py     ← escribe aquí
└── test_numeric.py  ← escribe aquí
```

`tests/test_example.py` trae **una** prueba completa con la estructura
Arrange–Act–Assert comentada paso a paso. Es tu plantilla. Los otros tres
archivos traen solo comentarios `TODO` con lo que hay que cubrir.

---

## Las funciones bajo prueba

| Función | Especificación resumida |
|---|---|
| `validate_username(name)` | Solo letras, de 5 a 12 caracteres, ambos extremos incluidos |
| `to_upper(text)` | Devuelve el texto en mayúsculas |
| `to_lower(text)` | Devuelve el texto en minúsculas |
| `count_words(text)` | Cuenta palabras separadas por espacios en blanco |
| `is_palindrome(text)` | ¿Se lee igual al derecho y al revés? Ignora espacios y mayúsculas |
| `is_leap_year(year)` | ¿Es año bisiesto en el calendario gregoriano? |
| `clamp(value, minimum, maximum)` | Recorta el valor al rango cerrado `[minimum, maximum]` |

La tabla es un resumen. **La especificación completa está en el docstring de
cada función**, incluyendo qué pasa con la cadena vacía, con los acentos y con
los extremos exactos.

---

## Qué tienes que entregar

1. **Pruebas para las siete funciones**, en los tres archivos `test_*.py`.
2. En `validate_username`, aplica de forma explícita y visible las dos
   técnicas de la clase:
   - **Particiones de equivalencia** — una prueba por clase: longitud `< 5`,
     longitud `5–12`, longitud `> 12`, y entradas que no son solo letras.
   - **Valores frontera** — los seis valores donde la validez cambia:
     `4, 5, 6` y `11, 12, 13`.

   Que se note en los nombres de las pruebas a qué clase o frontera
   corresponde cada una.
3. **Los dos defectos**, documentados en un archivo `HALLAZGOS.md` en la raíz
   del repositorio. Para cada uno:
   - la función y el archivo,
   - la entrada exacta que lo revela,
   - el resultado obtenido y el esperado según la especificación,
   - la línea del docstring que se incumple.

   **No corrijas el código fuente.** El entregable es la prueba que falla, no
   el arreglo. Una prueba que falla y demuestra el defecto vale; una nota que
   dice "creo que aquí hay un error" no.
4. Todo lo demás debe pasar. Si una prueba tuya falla y **no** corresponde a
   uno de los dos defectos, entonces la prueba está mal escrita: revísala
   contra el docstring.

**Formato de entrega:** (a definir por el catedrático)
**Fecha de entrega:** (a definir por el catedrático)

---

## Rúbrica

| Criterio | Qué se evalúa |
|---|---|
| **Cobertura de casos** | Las siete funciones tienen pruebas. Cada rama de la especificación y cada caso límite del docstring (vacío, cero, negativos, espacios, unicode) tiene al menos una prueba |
| **Técnica aplicada** | Particiones de equivalencia y valores frontera usadas de verdad en `validate_username`, con los seis valores frontera presentes y reconocibles |
| **Calidad de las pruebas** | Estructura Arrange–Act–Assert; nombres que describen el comportamiento; una prueba por comportamiento; el valor esperado escrito a mano, no calculado con la misma función que se prueba |
| **Detección de defectos** | Los dos defectos encontrados, cada uno demostrado por una prueba que falla, y documentados en `HALLAZGOS.md` |
| **El proyecto corre** | `uv sync` y `uv run pytest` funcionan en un clon limpio, sin pasos manuales extra |

Peso de cada criterio: (a definir por el catedrático)

---

## Reglas del juego

- **No modifiques `src/`.** El código bajo prueba se queda como está, defectos
  incluidos. Si lo cambias, no queda evidencia de que encontraste algo.
- **No borres ni edites `tests/test_example.py`.**
- Una prueba unitaria no usa red, ni base de datos, ni archivos, ni la hora
  del sistema. Ninguna de estas siete funciones lo necesita: si sientes que
  una prueba tuya lo requiere, está mal planteada.
- El valor esperado se escribe a mano. `assert to_upper("hola") == to_upper("hola")`
  no prueba nada.

---

## Si algo se rompe

| Síntoma | Qué hacer |
|---|---|
| `command not found: uv` | `uv` no quedó en el `PATH`. Cierra y abre la terminal, o reinstala |
| `ModuleNotFoundError: No module named 'lab_unit_testing'` | Corriste `pytest` a secas. Usa siempre `uv run pytest` |
| `no tests ran` | Los archivos deben llamarse `test_*.py` y las funciones `def test_...()` |
| El clon limpio ya falla | Reporta el problema: eso no debería pasar |
