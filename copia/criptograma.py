from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr

# def criptograma_game(jugador):
#     intentos = 1
#     aciertos = 0
#     p = 0 #son pistas
#     game = juego_criptograma
#     quiz = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente

#     recompensa = game['award']
#     reglas = game['rules']
#     print("Bienvendio al criptograma!")
#     print(f'Estas son las reglas del juego: {reglas}')
#     print(f'La recomensa de este juego es: "mensaje"')

#     texto = (quiz['question']).lower()
#     texto = texto.replace("á", "a")

#     desplazamiento = quiz['desplazamiento']
#     abc= "abcdefghijklmnopqrstuvwxyz"
#     cifrad = ""
#     for c in texto:
#         if c in abc:
#             cifrad = cifrad + abc[(abc.index(c)+desplazamiento)%(len(abc))]
#         else:
#             cifrad = cifrad + c


#     print("""Debes saber que el desplazamiento en  el abecedario es aleatorio y la logica del juego es de la siguiente manera:
#     Si el desplazamiento = 1
#     a = b
#     b = c
#     c = d
#     """)
#     print("\n")
#     print(f"El texto cifrado es: {cifrad}")
#     s= input("¿Cual es la palbra escondida?: ").lower()

#     while True:
#         if s == texto:
#             print(f"¡Adivinaste! la palabra era {texto} 🥳")
#             print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
#             print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
#             jugador.agregar_inv(recompensa)

#             salida = input('Escribe (f) para regresar: ')
#             while not salida == 'f':
#                 salida = input('Por favor, escribe (f) para regresar: ')
#             os.system('clear')
#             break
#         else:
#             intentos = intentos + 1         
#             aciertos = 0
#             print("No adivinaste 😕")
#             jugador.quitar_vidas(1)
#             print("Intentalo otra vez")
#             s = input("¿Cual es la palbra escondida?: ")
            
            

