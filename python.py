from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr

# def python_game(jugador):

intentos = 1
aciertos = 0
p = 0 #son pistas
game = juego_python
quiz = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente

recompensa = game['award']
reglas = game['rules']

print(f'Estas son las reglas del juego: {reglas}')
print(f'La recomensa de este juego es: {recompensa}')

pregunta = quiz['question']
frase  = "tengo en mi cuenta 50,00 $"
# print(pregunta)
print('\n')
print('\n')
hola = '355.157'
user_input = eval(input(f'{pregunta} {frase} =>'))
print(user_input)


# texto="la casa 24 roja es de otra propiedad."
# user_input = eval(input(f'Escribe el codigo en python para sacar los numeros enteros en la siguiente pregunta: \n (la variable del texto se llama texto) {texto} =>'))
# print(user_input)


# respuesta = validarlo con python