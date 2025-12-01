"""
funciones.py
Autor: Cristian Fernandez Cornejo
"""
# definimos la funcion esPalindromo
def esPalindromo(cadena):
    if not isinstance(cadena, str):
        raise TypeError("la entrada debe ser una cadena de texto")

    cadena_limpia = ''.join(ch.lower() for ch in cadena if ch.isalnum())

    if len(cadena_limpia) < 2:
        return False

    return cadena_limpia == cadena_limpia[::-1]
