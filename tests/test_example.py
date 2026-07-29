"""Ejemplo resuelto: la forma que debe tener cada prueba que escribas.

Este es el único archivo de pruebas que viene completo. Úsalo como plantilla
y escribe las tuyas en `test_username.py`, `test_text.py` y `test_numeric.py`.
"""

# Importamos solo la función que vamos a probar. Una prueba unitaria examina
# una unidad pequeña de código de forma aislada: sin red, sin base de datos,
# sin archivos.
from lab_unit_testing.text import to_upper


def test_to_upper_converts_lowercase_word_to_uppercase():
    """El nombre de la prueba describe el comportamiento esperado.

    Fórmula: test_<función>_<condición>_<resultado esperado>. Cuando una
    prueba falla, pytest imprime este nombre: debe bastar para saber qué se
    rompió sin abrir el archivo.
    """
    # --- Arrange (preparar) ---------------------------------------------
    # Definimos la entrada y el resultado que esperamos. Escribir el valor
    # esperado a mano —y no calcularlo con la misma función que probamos—
    # es lo que le da valor a la prueba.
    text = "hola"
    expected = "HOLA"

    # --- Act (actuar) ---------------------------------------------------
    # Ejecutamos la unidad bajo prueba: una sola llamada, sin lógica extra.
    result = to_upper(text)

    # --- Assert (verificar) ---------------------------------------------
    # Comparamos lo obtenido contra lo esperado. Un assert por comportamiento:
    # si necesitas cinco asserts distintos, probablemente necesitas cinco
    # pruebas.
    assert result == expected
