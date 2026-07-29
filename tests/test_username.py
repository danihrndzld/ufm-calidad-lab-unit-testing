"""Pruebas de validate_username. Escribe aquí las tuyas.

Especificación (léela en el docstring de la función antes de empezar):
solo letras, de 5 a 12 caracteres, ambos extremos incluidos.

Esta es la función donde debes aplicar de forma explícita las dos técnicas
de la clase: particiones de equivalencia y valores frontera.
"""

from lab_unit_testing.validators import validate_username

# =====================================================================
# TODO 1 · Particiones de equivalencia (una prueba por clase)
# ---------------------------------------------------------------------
#   - Clase inválida: longitud menor que 5.
#   - Clase válida:   longitud entre 5 y 12.
#   - Clase inválida: longitud mayor que 12.
#   - Clase inválida: contiene algo que no es letra (dígito, espacio,
#     guion, guion bajo, cadena vacía).
#
# TODO 2 · Valores frontera (donde la validez cambia)
# ---------------------------------------------------------------------
#   - Frontera inferior: 4, 5 y 6 caracteres.
#   - Frontera superior: 11, 12 y 13 caracteres.
#   Cada uno de esos seis valores merece su propia prueba con su propio
#   nombre. Los ejemplos con nombre propio (4 y 13) son tus pruebas
#   negativas: ahí es donde viven los defectos de "uno por uno".
#
# TODO 3 · Casos que la especificación deja escritos
# ---------------------------------------------------------------------
#   - ¿Qué pasa con la cadena vacía?
#   - ¿Qué pasa con letras acentuadas o con "ñ"?
#   - ¿Qué pasa con mayúsculas?
#
# Sugerencia: para construir una entrada de longitud exacta sin contar
# letras a mano, usa "a" * 12.
# =====================================================================
