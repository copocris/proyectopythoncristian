"""funciones.py
Autor: Cristian Fernandez Cornejo
Fecha: 30/11/2025
"""
import unicodedata

# definimos la funcion para quitar tildes

def quitar_tildes(cadena):
    return ''.join(
        ch for ch in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(ch) != 'Mn'
    )

# definimos la funcion esPalindromo
def esPalindromo(cadena):
    if not isinstance(cadena, str):
        raise TypeError("la entrada debe ser una cadena de texto")

    cadena_sin_tildes = quitar_tildes(cadena)
    
    cadena_limpia = ''.join(
        ch for ch in cadena_sin_tildes 
        if ch.isalnum()
    ).lower()

    return cadena_limpia == cadena_limpia[::-1]