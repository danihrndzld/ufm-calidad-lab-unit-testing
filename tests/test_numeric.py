"""Pruebas de las funciones numéricas. Escribe aquí las tuyas.

Lee el docstring de cada función antes de escribir la prueba: ahí está la
especificación contra la que decides si el resultado es correcto.
"""

from lab_unit_testing.numeric import clamp, is_leap_year

# =====================================================================
# TODO 1 · is_leap_year
# ---------------------------------------------------------------------
# La regla gregoriana tiene tres ramas. Cada rama necesita al menos un
# ejemplo, y las tres se cruzan en años concretos:
#   - Divisible entre 4 y nada más: 2024.
#   - No divisible entre 4: 2023.
#   - Divisible entre 100 pero no entre 400: 1900.
#   - Divisible entre 400: 2000.
#   - Un año fuera de tu década de siempre, por ejemplo 1600 o 2100.
#
# TODO 2 · clamp (valores frontera puros)
# ---------------------------------------------------------------------
#   - Un valor dentro del rango.
#   - Un valor por debajo del mínimo.
#   - Un valor por encima del máximo.
#   - Un valor exactamente igual al mínimo.
#   - Un valor exactamente igual al máximo.
#   - Justo un paso adentro y justo un paso afuera de cada extremo.
#   - Rangos con números negativos, y un rango donde mínimo == máximo.
#
# TODO 3 · clamp cuando la entrada es inválida
# ---------------------------------------------------------------------
# La especificación dice que clamp lanza ValueError si el mínimo es mayor
# que el máximo. Para probar que algo falla como debe, pytest ofrece:
#
#     import pytest
#
#     def test_clamp_rejects_inverted_range():
#         with pytest.raises(ValueError):
#             clamp(5, 10, 0)
#
# Escríbela tú y comprueba que pasa.
# =====================================================================
