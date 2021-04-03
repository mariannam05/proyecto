from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr

def python_game(jugador):
    intentos = 1
    aciertos = 0
    p = 0 #son pistas
    game = juego_python
    eleccion = choice(["p1", "p2"])
    quiz = game['questions'] 
    recompensa = game['award']

    #pregunta 1 de python
    if eleccion == 'p1':
        p1 = quiz[0]
        pregunta = p1['question']
        pista1 = p1['clue_1'] 
        pista2 = p1['clue_2']
        pista3 = p1['clue_3']
        # respuesta1 = int(float(frase.split(' ')[4].replace(',','.')))
        frase  = "tengo en mi cuenta 50,00 $"
        while True:
            user_input = eval(input(f'{pregunta} \n "{frase}"=> '))
            print(f'La respuesta a tu codigo es: {user_input}')
            print('\n')
            if user_input == 50:
                print('¡Tu respuesta es correcta!')
                print (f"Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
                jugador.agregar_inv(recompensa)
                print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
                print('\n')
                salida = input('Escribe (f) para regresar: ')
                while not salida == 'f':
                    salida = input('Por favor, escribe (f) para regresar: ')
                os.system('clear')
                break
            else:
                print('Tu respuesta es incorrecta')
                jugador.quitar_vidas(1/2)
                intentos = intentos + 1
                if jugador.pistas == 0:
                    print('No tienes mas pistas, sigue intentando tu solo...')
                    user_input = eval(input(f'{pregunta} {frase} =>'))
                else:
                    pistas = input('¿Quieres usar una pista?(s/n): ')
                    while not (pistas=='s' or pistas=='n'):
                        print('Ingresaste datos invalidos, intentalo otra vez')
                        pistas = input('¿Quieres usar una pista?(s/n): ')
                    if pistas == 's':
                        p = p + 1
                        jugador.pistas = jugador.pistas - 1
                        if p == 1:
                            print(pista1)
                            print('\n')
                        elif p==2:
                            print(pista2)
                            print('\n')
                        elif p==3:
                            print(pista3)
                            print('\n')
                        else:
                            print('Ya viste todas las pistas:')
                            print(pista1)
                            print(pista2)
                            print(pista3)
                            print('\n')
                    else:
                        continue
                        print('\n')
    #pregunta 2 de python
    else:
        p2 = quiz[1]
        pregunta = p2['question']
        frase = "\"oidutse ne al ortem aireinegni ed sametsis\""
        pista1 = p2['clue_1'] 
        while True:
            user_input = eval(input(f'{pregunta} \n "{frase}"=> '))
            print(f'La respuesta a tu codigo es: {user_input}')
            print('\n')
            if user_input == 'estudio en la metro ingenieria de sistemas':
                print('¡Tu respuesta es correcta!')
                print (f"Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
                print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
                jugador.agregar_inv(recompensa)
                print('\n')
                salida = input('Escribe (f) para regresar: ')
                while not salida == 'f':
                    salida = input('Por favor, escribe (f) para regresar: ')
                os.system('clear')
                break
            else:
                print('Tu respuesta es incorrecta')
                jugador.quitar_vidas(1/2)
                intentos = intentos + 1
                if jugador.pistas == 0:
                    print('No tienes mas pistas, sigue intentando tu solo...')
                    user_input = eval(input(f'{pregunta} {frase} =>'))
                else:
                    pistas = input('¿Quieres usar una pista?(s/n): ')
                    while not (pistas=='s' or pistas=='n'):
                        print('Ingresaste datos invalidos, intentalo otra vez')
                        pistas = input('¿Quieres usar una pista?(s/n): ')
                    if pistas == 's':
                        p = p + 1
                        jugador.pistas = jugador.pistas - 1
                        if p == 1:
                            print(pista1)
                            print('\n')
                        else:
                            print('Ya viste todas las pistas:')
                            print(pista1)
                            print('\n')
                    else:
                        continue
                        print('\n')

