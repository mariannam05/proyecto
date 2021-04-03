from Juego import Juego
from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr
from ahorcado import *

#clase hija de la clase juegos
#el otro archivo ahorcado.py contiene las funciones que complementan el juego
class Ahorcado(Juego):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')

    def ahorcado_game(self,jugador):
        game = juego_ahorcado
        quiz = choice(game['questions'])
        #datos extra del juego
        recompensa = game['award']
        #datos para la programacion del juego
        pregunta = quiz['question']
        respuesta = quiz['answer']
        pista1 = quiz['clue_1']
        pista2 = quiz['clue_2']
        pista3 = quiz['clue_3'] 


        AHORCADO = ['''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''']

        
        print('\n')
        print ('⸭⸭⸭⸭⸭⸭⸭⸭⸭ A H O R C A D O ⸭⸭⸭ (Version Unimetana) ⸭⸭⸭⸭⸭⸭⸭⸭⸭')
        print(pregunta)
        letraIncorrecta = ""
        letraCorrecta = ""
        respuesta = (quiz['answer']).lower() #palabra secreta a buscar
        intentos = 1
        p = 0 #cant de pistas usadas

        while True:
            tablero(AHORCADO, letraIncorrecta, letraCorrecta, respuesta)
            letra = elijeLetra(letraIncorrecta + letraCorrecta)

            if letra in respuesta: #si la letra ingresada esta en la respuesta
                letraCorrecta = letraCorrecta + letra
                letrasEncontradas = True
                for i in range(len(respuesta)):
                    if respuesta[i] not in letraCorrecta:
                        letrasEncontradas = False
                        break
                if letrasEncontradas:
                    print (f'¡Ganaste! La palabra secreta es "{respuesta}"!')
                    print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
                    jugador.agregar_inv(recompensa)
                    salida = input('Escribe (f) para regresar: ')
                    while not salida == 'f':
                        salida = input('Por favor, escribe (f) para regresar: ')
                    os.system('clear')
                    break


            else:       #si la letra no esta en la respuesta
                letraIncorrecta = letraIncorrecta + letra
                intentos = intentos + 1
                jugador.quitar_vidas(1/4)

                if jugador.pistas == 0:
                    print('No tienes mas pistas, sigue intentando tu solo...')
                    respuesta = input('→ ')
                else:
                    pistas = input('¿Quieres usar una pista?(s/n): ')
                    while not (pistas=='s' or pistas=='n'):
                        print('Ingresaste datos invalidos, intentalo otra vez')
                        pistas = input('¿Quieres usar una pista?(s/n): ')
                    if pistas == 's':
                        os.system('clear')
                        if intentos == 2:          
                            p = p + 1
                            jugador.pistas = jugador.pistas - 1
                            print('\n')
                            print('PISTA: ')
                            print(pista1)
                            continue
                        elif intentos == 3:
                            jugador.pistas = jugador.pistas - 1
                            p = p + 1
                            print('\n')
                            print('PISTA: ')
                            print(pista2)
                            continue
                        elif intentos == 4:
                            jugador.pistas = jugador.pistas - 1
                            p = p + 1
                            print('\n')
                            print('PISTA: ')
                            print(pista3)
                            continue
                        else:
                            jugador.pistas = jugador.pistas - 1
                            print('\n')
                            print('Ya viste todas las pistas: ')
                            print(pista1)
                            print(pista2)
                            print(pista3)
                            continue
                    else:
                        continue
                # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
                if len(letraIncorrecta) == len(AHORCADO) - 1:
                    tablero(AHORCADO, letraIncorrecta, letraCorrecta, respuesta)
                    print ('¡te quedaste sin letras!\nDespues de {str(len(letraIncorrecta))} letras erroneas y {str(len(letraCorrecta))} letras correctas, la palabra era {respuesta} ')
                    break
