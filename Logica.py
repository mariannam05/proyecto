from Juego import Juego
from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr
#clase hija de la clase juegos
class Logica(Juego):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')

    def logica_booleana_game(elf,jugador):
        game = juego_booleana
        quiz = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente
        recompensa = game['award']

        print(f'Para jugar necesitas tener en tu inventario {requerido}!!')

        pregunta = quiz['question']
        respuesta1 = quiz['answer']
        respuesta2 = lambda x: 'True' if x == 'False' else 'False'

        print(f'''Pregunta: {pregunta}

        a) {respuesta2(respuesta1)}
        b) {respuesta1}
        Respuesta:
        ''')
        r = input('(a/b)→ ').lower()
        while r != 'a' and r != 'b':
            print('Ingresaste datos invalidos, intentalo otra vez')
            r = input('(a/b)→ ').lower()

        while True:
            if r == 'b':
                print('¡Tu respuesta es correcta!')
                print (f"Felicitaciones! Haz ganado un {recompensa}, lo puedes ver en tu inventario!")
                jugador.agregar_inv(recompensa)
                salida = input('Escribe (f) para regresar: ')
                while not salida == 'f':
                    salida = input('Por favor, escribe (f) para regresar: ')
                os.system('clear')
                break

            else:
                print('Tu respuesta es incorrecta')
                jugador.quitar_vidas(1/2)