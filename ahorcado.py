import random
from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr

def elijeLetra(algunaLetra):
            # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
            while True:
                print ('Adivina una letra:')
                letra = input()
                letra = letra.lower()
                if len(letra) != 1:
                    print ('Introduce una sola letra.') 
                elif letra in algunaLetra:
                    print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
                elif letra not in 'abcdefghijklmnopqrstuvwxyz':
                    print ('Elije una letra.')
                else:
                    return letra

def tablero(AHORCADO, letraIncorrecta, letraCorrecta, respuesta):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(respuesta)
    for i in range(len(respuesta)): # Remplaza los espacios en blanco por la letra bien escrita
        if respuesta[i] in letraCorrecta:
            espacio = espacio[:i] + respuesta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")