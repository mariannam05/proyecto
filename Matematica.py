from Juego import Juego
from api import *
import os
from random import choice
from sympy import *
from scipy.misc import derivative
from math import pi
from fractions import Fraction


#clase hija de la clase juegos
class Matematica(Juego):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')

    def mate_game(self,jugador):
        game = juego_mate
        quiz = choice(game['questions']) 
        pregunta = quiz['question']
        p = 0       #pistas
        pista = quiz['clue_1']
        recompensa = game['award']

        frase = pregunta.split(' ')         #convertimos el string en una lista para sacar la variable 
        variable = frase[7]         #ver si la variable es pi o pi/3
        variable = eval(variable)     #ver el resultado final de la variable(3,14 o 1,048) 
        intentos = 1

        x = Symbol('x')
        funcion = pregunta.replace('Calcula la derivada de la función en ','').replace('pi', '').replace('/3','').replace('f(x)=', '').replace('sen', 'sin')
        funcion = eval(funcion)

        print(f'Variable a evaluar la derivada: {variable}')
        print(f'Funcion donde evaluará la derivada: {funcion}')
        respuesta = diff(funcion, x).subs(x,variable)                                   #derivacion de la funcion aleatoria
        respuesta = round(respuesta, 1)                     #redondeamos a un decimal la respuesta obtenida de la derivacion
        respuesta = str(respuesta)
        pregunta_acomodada = pregunta.replace('letra incorrecta', 'intento fallido')        #porque en el api dice letra incorrecta entonces lo cambiamos
        print(pregunta_acomodada)
        answer = input('→ ')
        answer = answer.replace(',', '.')
        answer = eval(answer)
        answer = round(answer, 1)
        answer = str(answer)
        while True:
            if answer == respuesta:
                print('¡Tu respuesta es correcta!')
                print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos y usaste {p} pistas.")
                print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
                jugador.agregar_inv('Vida Extra Mate')
                jugador.agregar_vida(1)
                salida = input('Escribe (f) para regresar: ')
                while not salida == 'f':
                    salida = input('Por favor, escribe (f) para regresar: ')
                os.system('clear')
                break

            elif answer != respuesta:
                intentos = intentos + 1
                print('RESPUESTA INCORRECTA')
                jugador.quitar_vidas(1/4)
                if jugador.pistas == 0:
                    print('No tienes mas pistas, sigue intentando tu solo...')
                    answer = input('→ ')
                else:
                    pistas = input('¿Quieres usar una pista?(s/n): ')
                    while not (pistas=='s' or pistas=='n'):
                        print('Ingresaste datos invalidos, intentalo otra vez')
                        pistas = input('¿Quieres usar una pista?(s/n): ')

                    if pistas == 's':
                        if p == 0:
                            p = p + 1
                            jugador.pistas = jugador.pistas - 1
                            print(pista)
                            answer = input('→ ')
                        else:
                            print('No existen más pistas para esta pregunta')
                            answer = input('→ ')
                    else:
                        answer = input('→ ')


                
                
                