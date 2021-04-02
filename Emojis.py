from Juegos import Juegos
from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr

#clase hija de la clase juegos

class Emojis(Juegos):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')

    def emojis_game(self,jugador):
        game = juego_dibujos
        quiz = game['questions']
        #datos del juego
        recompensa = game['award']
    
        eleccion = choice(["p1", "p2"])
        intentos = 1
        aciertos = 0

        if eleccion == 'p1':        #pregunta 1 de la api, no se puede hacer de otra forma ya que los resultados son diferentes y no los tiene la api
            p1 = quiz[0]
            respuesta1 = 67
            print(f'''
        {p1}
        ¿Cuánto vale la ultima fila?: ''')
            respuesta = input('→ ')
            while not respuesta.isnumeric():
                print('Ingresaste datos invalidos, intentalo otra vez')
                respuesta = input('→ ')
            while True:
                if int(respuesta) == respuesta1:
                    aciertos = aciertos + 1
                    print('¡Tu respuesta es correcta!')
                    print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos.")
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
                    respuesta = input('→ ')

        elif eleccion == 'p2':              #pregunta 2 de la api
            p2 = quiz[1]
            respuesta2 = 41
            print(f'''
        {p2}
        ¿Cuánto vale la ultima fila?: ''')
            respuesta = input('→ ')
            while not respuesta.isnumeric():
                print('Ingresaste datos invalidos, intentalo otra vez')
                respuesta = input('→ ')
            while True:
                if int(respuesta) == respuesta2:
                    aciertos = aciertos + 1
                    print('¡Tu respuesta es correcta!')
                    print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos.")
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
                    respuesta = input('→ ')