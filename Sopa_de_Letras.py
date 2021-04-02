from Juegos import Juegos
from api import *
import os
import string 
from random import randrange, choice
from colored import fg, bg, attr
from sopaletras import *
#clase hija de la clase juegos

class Sopa_de_letras(Juegos):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')
    

    def sopa_game(self,jugador):
        intentos = 0
        aciertos = 0
        p = 0 #son pistas
        game = juego_sopa
        recompensa = game['award']
        quiz = choice(game['questions'])
        pista1 = quiz['clue_1']
        pista2 = quiz['clue_2']
        pista3 = quiz['clue_3']
        acertadas = []
        grid_size = 15

        palabras = [quiz['answer_1'].upper(), quiz['answer_2'].upper(), quiz['answer_3'].upper()] 


        grid = [[choice(string.ascii_uppercase) for i in range(grid_size)] for j in range(grid_size)] #genera una matriz de nxn con letras aleatorias
        for palabra in palabras:
            grid = agragar_palabra(palabra, grid)


        print('\n'.join(map(lambda row: ' '.join(row), grid))) #muestra sopa de letras completa

        while jugador.vidas > 0:
            pistas = input('¿Quieres usar una pista?(s/n): ').lower()
            while not (pistas=='s' or pistas=='n'):
                print('Ingresaste datos invalidos, intentalo otra vez')
                pistas = input('¿Quieres usar una pista?(s/n): ').lower()

            if pistas == 's':
                if jugador.pistas > 0:
                    jugador.pistas = jugador.pistas - 1
                    p +=1
                    if p == 1:
                        print(pista1)
                    elif p == 2:
                        print(pista2)    
                    elif p == 3:
                        print(pista3)
                    else:
                        print('Ya viste todas las pistas: ')
                        print(pista1)
                        print(pista2)
                        print(pista3)
                else:
                    print('No tienes mas pistas, sigue intentando tu solo...')

            if pistas == 'n':
                print('\n')
                resp = input('Ingrese una palabra: ').upper()
                intentos = intentos + 1
                while not resp.isalpha():
                    print('Ingresaste datos invalidos, intentalo otra vez')
                    resp = input('Ingrese una palabra: ').upper()

                if resp in acertadas:
                    print('Ya adivinaste esta palabra')     #verificar que no acierte una palabra 2 veces

                elif resp in palabras:      #verificar si es correcta
                    acertadas.append(resp)
                    print(f'PALABRA CORRECTA {len(acertadas)}/{len(palabras)}')
                    print(f'Palabras Adivinadas: {" ".join(acertadas)}')
                    if len(acertadas) == len(palabras):
                        print('\n')
                        print('¡Adivinaste todas las palabras! 🥳')
                        print (f"Felicitaciones! Adivinaste todas las palabras en {intentos} intentos y usaste {p} pistas.")
                        print(f'Haz ganado una {recompensa}, lo puedes ver en tu inventario!')
                        jugador.agregar_vida(1)
                        jugador.agregar_inv('Vida Extra Sopa')
                        print('\n')
                        salida = input('Escribe (f) para regresar: ')
                        while not salida == 'f':
                            salida = input('Por favor, escribe (f) para regresar: ')
                        os.system('clear')
                        break

                else:           #es incorrecta la respuesta
                    print('PALABRA INCORRECTA')
                    jugador.quitar_vidas(1/2)