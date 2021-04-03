from Juegos import Juegos
from api import *
import os
from random import randrange, choice, sample
from colored import fg, bg, attr

#clase hija de la clase juegos

class Mezclada(Juegos):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')

    def mezclada_game(self, jugador):
        game = juego_mezclada
        recompensa = game['award']
        azar = choice(game['questions']) 
        pregunta = azar['question']
        categoria = azar['category']
        palabras = azar['words']
        desordenadas = []
        acertadas = []

        for palabra in palabras:
            lista = list(palabra)
            lista_desor = sample(lista, len(lista))
            palabra_desor = ''.join(lista_desor)
            desordenadas.append(palabra_desor)

        print(f'\nCategoría: {categoria}\n')
        print('Palabras: ')
        for p in desordenadas:
            print(f' > {p}')
        while True:
            print('\n')
            r = input('=> ').lower()
            while not r.isalpha():
                print('Ingreso inválido')
                r = input('=> ').lower()
            if r in acertadas:
                print('Ya adivinaste esta palabra')
            elif r in palabras:
                acertadas.append(r)
                print(f'PALABRA CORRECTA {len(acertadas)}/{len(palabras)}')
                print(f'Palabras Adivinadas: {" ".join(acertadas)}')
            else:
                print('PALABRA INCORRECTA')
                print('menos media vida')
                jugador.quitar_vidas(1/2) 

            if len(acertadas) == len(palabras):
                print('\n')
                print('¡Tu respuesta es correcta!')
                jugador.agregar_inv(recompensa)
                print(f'Haz ganado una {recompensa} que es {recompensa}, lo puedes ver en tu inventario!')
                print('\n')
                salida = input('Escribe (f) para regresar: ')
                while not salida == 'f':
                    salida = input('Por favor, escribe (f) para regresar: ')
                os.system('clear')
                break

            