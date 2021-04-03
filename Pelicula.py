from Juego import Juego

import os
from random import randrange, choice, sample
from colored import fg, bg, attr

#clase hija de la clase juegos
class Pelicula(Juego):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')
    
    def peliculas_game(self, jugador):
        game = {
            'pregunta' : [
                {
                    "question": "👸❄⛄🦌",
                    "answer": "frozen",
                    "clue_1": "pelicula de disney",
                    "clue_2": "libre soy"
                },
                {
                    "question": "🚢👩‍❤️‍💋‍👨💔🧊",
                    "answer": "titanic",
                    "clue_1": "un iceberg",
                    "clue_2": "una tabla de madera"
                },
                {
                "question": "🌙🚲👉👈👽",
                "answer": "et",
                "clue_1": "quiere ir a casa",
                "clue_2": "es un alienigena"
                },
                {
                "question": "😭🦁👑🐗",
                "answer": "el rey leon",
                "clue_1": "es en la selva",
                "clue_2": "hakuna matata"
                },
                {
                "question": "🧜‍♀️🚫🦵👩‍❤️‍💋‍👨",
                "answer": "la sirenita",
                "clue_1": "se queda sin voz",
                "clue_2": "bajo del mar"
                },
                {
                "question": "🚗💨🚙💨😡",
                "answer": "rapidos y furiosos",
                "clue_1": "en todas las peliculas estan enojados",
                "clue_2": "carreras de carros"
                }
            ]
        }

        azar = choice(game['pregunta']) 
        pregunta = azar['question']
        respuesta = azar['answer']
        pista1 = azar['clue_1']
        pista2 = azar['clue_2']


        intentos = 1
        aciertos = 0
        p = 0 #cant de pistas usadas
        recompensa = 'Ganar el juego'
        print('Este es un juego de Adivinar la pelicula segun los emojis, debes responder correctamente la pregunta!')
        print('\n')

        print(f"Pregunta: {pregunta}")
        resp = input('→ ').lower()
        while not respuesta.isalpha:
            print('Ingresaste datos invalidos, intentalo otra vez')
            resp = input('→ ').lower()
        while True:
            if resp == respuesta:
                aciertos = aciertos + 1
                print('¡Tu respuesta es correcta!')
                print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
                print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
                os.system('clear')
                break
            else:
                intentos = intentos + 1
                aciertos = 0
                print('Tu respuesta es incorrecta')
                jugador.quitar_vidas(1)
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
                            resp = input('→ ').lower()
                        elif p == 1:
                            p = p + 1
                            print('\n')
                            print(pista2)
                            resp = input('→ ').lower()
                        else:
                            p = p + 1
                            print('\n')
                            print('Ya viste todas las pistas: ')
                            print(pista1)
                            print(pista2)
                            resp = input('→ ').lower()
                    else:
                        resp = input('→ ').lower()