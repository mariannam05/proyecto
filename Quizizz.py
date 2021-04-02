from Juegos import Juegos
from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr

#clase hija de la clase juegos

from Juegos import Juegos
from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr
from ahorcado import *

#clase hija de la clase juegos
#el otro archivo ahorcado.py contiene las funciones que complementan el juego
class Quizizz(Juegos):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')

    def game_q(self,jugador):
        intentos = 1
        aciertos = 0
        p = 0 #son pistas
        game = juego_quizizz
        quiz = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente

        recompensa = game['award']
        reglas = game['rules']

        pregunta = quiz['question']
        respuesta1 = quiz['correct_answer']
        respuesta2 = quiz['answer_2']
        respuesta3 = quiz['answer_3']
        respuesta4 = quiz['answer_4']
        pista = quiz['clue_1']
        print(f'''
        Pregunta: {pregunta}
        opciones:
        a) {respuesta1}            b) {respuesta3}
        c) {respuesta2}            d) {respuesta4}
        ''')
        respuesta = input('(a/b/c/d)→ ')
        while not (respuesta=='a' or respuesta=='b' or respuesta=='c' or respuesta=='d'):
            print('Ingresaste datos invalidos, intentalo otra vez')
            respuesta = input('→ ')
        while True:
            if respuesta == 'a':
                aciertos = aciertos + 1
                print('¡Tu respuesta es correcta!')
                print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
                print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
                jugador.agregar_inv(recompensa)
                salida = input('Escribe (f) para regresar: ')
                while not salida == 'f':
                    salida = input('Por favor, escribe (f) para regresar: ')
                os.system('clear')
                break
            else:
                intentos = intentos + 1         #revisar los intentos en esta pregunta pero si te quita las pistas todo bien solo eso!
                aciertos = 0
                print('Tu respuesta es incorrecta')
                jugador.quitar_vidas(1/2)

                if jugador.pistas == 0:
                    print('No tienes mas pistas, sigue intentando tu solo...')
                    respuesta = input('→ ')
                else:
                    pistas = input('¿Quieres usar una pista?(s/n): ')
                    while not (pistas=='s' or pistas=='n'):
                        print('Ingresaste datos invalidos, intentalo otra vez')
                        pistas = input('¿Quieres usar una pista?(s/n): ')

                    if pistas == 's':
                        p = p + 1
                        jugador.pistas = jugador.pistas - 1
                        print(pista)
                        respuesta = input('→ ')
                    else:
                        respuesta = input('→ ')




