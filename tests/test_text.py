"""Pruebas de las funciones de texto. Escribe aquí las tuyas.

Lee el docstring de cada función antes de escribir la prueba: ahí está la
especificación contra la que decides si el resultado es correcto.
"""

from lab_unit_testing.text import count_words, is_palindrome, to_lower, to_upper

# =====================================================================
# TODO 1 · to_upper y to_lower
# ---------------------------------------------------------------------
#   - Una palabra normal (ya tienes el ejemplo en test_example.py).
#   - Cadena vacía.
#   - Texto que ya venía en el caso contrario.
#   - Texto mezclado: "HoLa".
#   - Caracteres sin mayúscula ni minúscula: dígitos, signos de puntuación.
#   - Letras acentuadas y "ñ".
#
# TODO 2 · count_words
# ---------------------------------------------------------------------
#   - Dos palabras separadas por un espacio.
#   - Una sola palabra.
#   - Cadena vacía.
#   - Cadena que solo tiene espacios.
#   - Varios espacios seguidos entre dos palabras.
#   - Espacios al inicio y al final.
#   - Separadores que no son espacio: tabulador (\t), salto de línea (\n).
#
# TODO 3 · is_palindrome
# ---------------------------------------------------------------------
#   - Un palíndromo de una sola palabra.
#   - Un palíndromo con espacios: "anita lava la tina".
#   - Algo que no es palíndromo.
#   - Cadena vacía y cadena de un solo carácter.
#   - Mismo texto con distinta capitalización.
#   - Un caso con acentos: ¿"esta" y "está" son iguales para esta función?
#     La especificación lo responde.
# =====================================================================
