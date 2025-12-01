"""charfun.py
Autor: Cristian Fernandez Cornejo
Fecha: 30/11/2024
"""

from modulo1.funciones import esPalindromo

while True:
    # pedimos una frase al usuario 
    frase = input("Introduce una frase (o escribe 'salir' para terminar): ")

    # salimos si ponemos salir en el terminal
    if frase.lower() == "salir":
        print("Programa finalizado.")
        break

    # usamos la funcion del modulo 1
    if esPalindromo(frase):
        print("La frase es palíndroma.")
    else:
        print("La frase no es palíndroma.")

