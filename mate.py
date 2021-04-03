from Juegos import Juegos
from api import *
import os
from random import choice
from sympy import *
from scipy.misc import derivative
from math import pi
from fractions import Fraction


#clase hija de la clase juegos
# class Numeros(Juegos):
#     def __init__(self,name, reglas, recompensa, position, cuarto):
#         self.cuarto = cuarto
#         super().__init__(name,reglas,recompensa,position)
    
#     def mostrar_cuarto(self):
#         print(f'Esta en el objeto: {self.cuarto}')

#     def mate_game(self,jugador):

# intentos = 1
# aciertos = 0
# p = 0 #son pistas
# game = juego_mate

# azar = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente
# recompensa = game['award']
# pregunta = azar['question']
# respuesta1 = azar['answer']
# pista1 = azar['clue_1']
# answers = ['-0.5', '-0,5', '-0.50', '-0,50','-0.20', '-0,20', '-0.2', '-0,2', '-3.9', '-3,9']
# print("Pregunta: {} ".format(pregunta))
# novalido = [',','!','.','"','-','']

# while True:
#     user_input = input('=> ')
#     while user_input.isalpha() or user_input.isspace() or user_input in novalido:
#         print('Ingresaste datos invalidos, intentelo nuevamente: ')
#         user_input = input('=> ')
#     if not user_input in answers:
#         intentos = intentos + 1
#         aciertos = 0
#         print('Tu respuesta es incorrecta')
#         jugador.quitar_vidas(1/4)
#         if jugador.pistas == 0:
#             print('No tienes mas pistas, sigue intentando tu solo...')
#         else: 
#             pistas = input('¿Quieres usar una pista?(s/n): ')
#             while not (pistas=='s' or pistas=='n'):
#                 print('Ingresaste datos invalidos, intentalo otra vez')
#                 pistas = input('¿Quieres usar una pista?(s/n): ')
#             if pistas == 's':
#                 if p == 0:          
#                     p = p + 1
#                     print('\n')
#                     print(pista1)
#                     respuesta = input('→ ')
#                 elif p == 1:
#                     p = p + 1
#                     print('\n')
#                     print(pista2)
#                     respuesta = input('→ ')
#                 elif p == 2:
#                     p = p + 1
#                     print('\n')
#                     print(pista3)
#                     respuesta = input('→ ')
#                 else:
#                     p = p + 1
#                     print('\n')
#                     print('Ya viste todas las pistas: ')
#                     print(pista1)
#                     print(pista2)
#                     print(pista3)
#                     respuesta = input('→ ')
#             else:
#                 respuesta = input('→ ')
    
#     else:
#         aciertos = aciertos + 1
#         print('¡Tu respuesta es correcta!')
#         print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
#         print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
#         jugador.agregar_inv(recompensa)
#         salida = input('Escribe (f) para regresar: ')
#         while not salida == 'f':
#             salida = input('Por favor, escribe (f) para regresar: ')
#         os.system('clear')
#         break


game = juego_mate
quiz = choice(game['questions']) 
pregunta = quiz['question']
pistas_usadas = 0
pista = quiz['clue_1']
recompensa = game['award']
v = pregunta.split(' ') #lista
v = v[7] #variable
v = eval(v)
x = Symbol('x')
fn = pregunta.replace('Calcula la derivada de la función en ','') 
fn = fn.replace('pi', '')
fn = fn.replace('/3','')
fn = fn.replace('f(x)=', '')
fn = fn.replace('sen', 'sin')
fn = eval(fn)
print(f'variable {v}, funcion {fn}')
respuesta = diff(fn, x).subs(x,v)                                   #(derivative(fn, v , dx=1e-5))
respuesta = round(respuesta, 1)
respuesta = str(respuesta)
print(pregunta.replace('letra incorrecta', 'intento fallido'))

while True:
    hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
    while hint != 's' and hint != 'n':
        print('Ingreso inválido')
        hint = input('¿Deseas usar una pista? [S] si [N] no\n>>').lower()
    if hint == 's':
        # if player.hints > 0:
            
        if pistas_usadas == 0:
            print(pista) 
            player.substract_hints(1)
            pistas_usadas +=1  
        else:
            print('No existen más pistas para esta pregunta')
        # else:
        #     print('No tienes pistas disponibles para este juego')
    if hint == 'n':
        answer = input('Respuesta: ')
        while answer.isalpha():
            print('La respuesta debe ser un número')
            answer = input('Respuesta: ')
        answer = answer.replace(',', '.')
        answer = eval(answer)
        answer = round(answer, 1)
        answer = str(answer)
        
        if answer == respuesta:
            print('RESPUESTA CORRECTA')
            break
            # player.add_to_inventory('calculadora')
            # player.add_lives(1)
            
        elif answer != respuesta:
            print('RESPUESTA INCORRECTA')
            print(f'La respuesta correcta era {respuesta}')
            # player.substract_lives(1/4)
        