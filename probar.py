# frase = "oidutse ne al ortem aireinegni ed sametsis"

# f = " ".join([frase.split(' ')[0][::-1],frase.split(' ')[1][::-1],frase.split(' ')[2][::-1],frase.split(' ')[3][::-1],frase.split(' ')[4][::-1],frase.split(' ')[5][::-1],frase.split(' ')[6][::-1]])


# from sympy import * 
# x, y = symbols('x y')
# gfg_exp = sin(x)*cos(x)
  
# print("Before Differentiation : {}".format(gfg_exp))
  
# # Use sympy.diff() method
# dif = diff(gfg_exp, x)
  
# print("After Differentiation : {}".format(dif))

from sympy import sin, cos, tan
from scipy.misc import derivative
from math import pi
from fractions import Fraction
from api import *
from random import randrange, choice, sample

# f= lambda x: sin(x)/2
# func = 'sin(x)/2'
# print(f'funcion: {func}')
# result = (derivative(f,pi, dx=1e-14))
# m = round(result, 1)
# r = float(m)
# a = Fraction(r)
# print(f'1) Sin fraccion: {m}')
# # print(f'1)Con fraccion: {str(Fraction(r))}')

f= lambda x: ((cos(x))/2) - ((tan(x))/5)
func = '((cos(x))/2) - ((tan(x))/5)'
print(f'funcion: {func}')
result2 = (derivative(f,pi, dx=1e-14))
m2 = round(result2, 2)
r2 = float(m2)
a2 = Fraction(r2)
print(f'2) Sin fraccion: {m2}')
# print(f'2)Con fraccion: {str(Fraction(r2))}')

# f = lambda x: ((sin(x))/5) - tan(x)
# func = '((sin(x))/5) - tan(x)'
# print(f'funcion: {func}')
# result2 = (derivative(f,(pi/3), dx=1e-14))
# m2 = round(result2, 2)
# r2 = float(m2)
# a2 = Fraction(r2)
# print(f'2) Sin fraccion: {m2}')
# # print(f'2)Con fraccion: {str(Fraction(r2))}')



# n = input(': ')
# while not (int(n) < 0 or int(n) > 0):
#     print('error')
#     n = input(': ')
# print('bien')

# x = "Calcula la derivada de la función evaluada en pi  f(x)=((sen(x))/2)"
# a = x.split(' ')
# q = a[-1]
# f = q.split('=')
# i = f[-1]
# print(i)

# intentos = 1
# aciertos = 0
# p = 0 
# game = juego_python
# azar = choice(game['questions']) 
# recompensa = game['award']
# pregunta = azar['question']
# respuesta1 = azar['answer']
# pista1 = azar['clue_1']
# pista2 = azar['clue_2']
# pista3 = azar['clue_3']

# print(pregunta)


# recompensa = game['award']
# #pregunta 1 de python
# if eleccion == 'p1':
#     p1 = quiz[0]
#     pregunta = p1['question']
#     pista1 = p1['clue_1'] 
#     pista2 = p1['clue_2']
#     pista3 = p1['clue_3']
#     # respuesta1 = int(float(frase.split(' ')[4].replace(',','.')))
#     frase  = "tengo en mi cuenta 50,00 $"
#     while True:
#         user_input = eval(input(f'{pregunta} \n "{frase}"=> '))
#         print(f'La respuesta a tu codigo es: {user_input}')
#         print('\n')
#         if user_input == 50:
#             print('¡Tu respuesta es correcta!')
#             print (f"Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
#             jugador.agregar_inv(recompensa)
#             print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
#             print('\n')
#             salida = input('Escribe (f) para regresar: ')
#             while not salida == 'f':
#                 salida = input('Por favor, escribe (f) para regresar: ')
#             os.system('clear')
#             break
#         else:
#             print('Tu respuesta es incorrecta')
#             jugador.quitar_vidas(1/2)
#             intentos = intentos + 1
#             if jugador.pistas == 0:
#                 print('No tienes mas pistas, sigue intentando tu solo...')
#                 user_input = eval(input(f'{pregunta} {frase} =>'))
#             else:
#                 pistas = input('¿Quieres usar una pista?(s/n): ')
#                 while not (pistas=='s' or pistas=='n'):
#                     print('Ingresaste datos invalidos, intentalo otra vez')
#                     pistas = input('¿Quieres usar una pista?(s/n): ')
#                 if pistas == 's':
#                     p = p + 1
#                     jugador.pistas = jugador.pistas - 1
#                     if p == 1:
#                         print(pista1)
#                         print('\n')
#                     elif p==2:
#                         print(pista2)
#                         print('\n')
#                     elif p==3:
#                         print(pista3)
#                         print('\n')
#                     else:
#                         print('Ya viste todas las pistas:')
#                         print(pista1)
#                         print(pista2)
#                         print(pista3)
#                         print('\n')
#                 else:
#                     continue
#                     print('\n')
# #pregunta 2 de python
# else:
#     p2 = quiz[1]
#     pregunta = p2['question']
#     frase = "oidutse ne al ortem aireinegni ed sametsis"
#     # respuesta2 = " ".join([frase.split(' ')[0][::-1],frase.split(' ')[1][::-1],frase.split(' ')[2][::-1],frase.split(' ')[3][::-1],frase.split(' ')[4][::-1],frase.split(' ')[5][::-1],frase.split(' ')[6][::-1]])
#     pista1 = p2['clue_1'] 
#     while True:
#         user_input = eval(input(f'{pregunta} \n "{frase}"=> '))
#         print(f'La respuesta a tu codigo es: {user_input}')
#         print('\n')
#         if user_input == 'estudio en la metro ingenieria de sistemas':
#             print('¡Tu respuesta es correcta!')
#             print (f"Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
#             print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
#             jugador.agregar_inv(recompensa)
#             print('\n')
#             salida = input('Escribe (f) para regresar: ')
#             while not salida == 'f':
#                 salida = input('Por favor, escribe (f) para regresar: ')
#             os.system('clear')
#             break
#         else:
#             print('Tu respuesta es incorrecta')
#             jugador.quitar_vidas(1/2)
#             intentos = intentos + 1
#             if jugador.pistas == 0:
#                 print('No tienes mas pistas, sigue intentando tu solo...')
#                 user_input = eval(input(f'{pregunta} {frase} =>'))
#             else:
#                 pistas = input('¿Quieres usar una pista?(s/n): ')
#                 while not (pistas=='s' or pistas=='n'):
#                     print('Ingresaste datos invalidos, intentalo otra vez')
#                     pistas = input('¿Quieres usar una pista?(s/n): ')
#                 if pistas == 's':
#                     p = p + 1
#                     jugador.pistas = jugador.pistas - 1
#                     if p == 1:
#                         print(pista1)
#                         print('\n')
#                     else:
#                         print('Ya viste todas las pistas:')
#                         print(pista1)
#                         print('\n')
#                 else:
#                     continue
#                     print('\n')
# # ep =expand(((sin(pi))/2))
# # print"Antes de la derivada: {}".format(exp))

# # # Use sympy.diff() method
# # dif = diff(exp, pi)
  
# # print("Despues de la derivada: {}".format(dif))