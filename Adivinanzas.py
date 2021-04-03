from Juegos import Juegos
from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr
#clase hija de la clase juegos

class Adivinanzas(Juegos):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')
    
    def adivinanzas_game(self, jugador):
        intentos = 1
        aciertos = 0
        p = 0 #cant de pistas usadas
        game = juego_adivinanzas
        azar = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente
        recompensa = game['award']

        print('Este es un juego de adivinanzas, debes responder correctamente la pregunta!')
        print('\n')

        pregunta = azar['question']
        respuesta1 = azar['answers']
        pista1 = azar['clue_1']
        pista2 = azar['clue_2']
        pista3 = azar['clue_3']

        print("Pregunta: {} ".format(pregunta))
        respuesta = input('→ ')
        while not respuesta.isalpha:
            print('Ingresaste datos invalidos, intentalo otra vez')
            respuesta = input('→ ')

        while True:
                if respuesta in respuesta1:
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
                    intentos = intentos + 1
                    aciertos = 0
                    print('Tu respuesta es incorrecta')
                    jugador.quitar_vidas(1/2)

                    if jugador.pistas == 0:
                        print('No tienes mas pistas, sigue intentando tu solo...')

                    else: 
                        pistas = input('¿Quieres usar una pista?(s/n): ')
                        while not (pistas=='s' or pistas=='n'):
                            print('Ingresaste datos invalidos, intentalo otra vez')
                            pistas = input('¿Quieres usar una pista?(s/n): ')

                        if pistas == 's':
                            if p == 0:          
                                p = p + 1
                                print('\n')
                                print(pista1)
                                respuesta = input('→ ')
                            elif p == 1:
                                p = p + 1
                                print('\n')
                                print(pista2)
                                respuesta = input('→ ')
                            elif p == 2:
                                p = p + 1
                                print('\n')
                                print(pista3)
                                respuesta = input('→ ')
                            else:
                                p = p + 1
                                print('\n')
                                print('Ya viste todas las pistas: ')
                                print(pista1)
                                print(pista2)
                                print(pista3)
                                respuesta = input('→ ')
                        else:
                            respuesta = input('→ ')


    