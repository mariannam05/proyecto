from api import *
from random import randrange, choice
import os

def adivinanzas_game(jugador):
    intentos = 1
    aciertos = 0
    p = 0 #cant de pistas usadas
    game = juego_adivinanzas
    azar = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente
    requerido = game['requirement']
    recompensa = game['award']
    reglas = game['rules']

    print('Este es un juego de adivinanzas, debes responder correctamente la pregunta!')
    print(f'Estas son las reglas del juego: {reglas}')
    print(f'La recomensa de este juego es: {recompensa}')
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
                respuesta = input('→ ')

                if jugador.pistas == 0:
                    print('No tienes mas pistas, sigue intentando tu solo...')

                else: 
                    pistas = input('¿Quieres usar una pista?(s/n): ')
                    while not (pistas=='s' or pistas=='n'):
                        print('Ingresaste datos invalidos, intentalo otra vez')
                        pistas = input('¿Quieres usar una pista?(s/n): ')

                    if pistas == 's':
                        if intentos == 2:          
                            p = p + 1
                            print('\n')
                            print(pista1)
                            respuesta = input('→ ')
                        elif intentos == 3:
                            p = p + 1
                            print('\n')
                            print(pista2)
                            respuesta = input('→ ')
                        elif intentos == 4:
                            p = p + 1
                            print('\n')
                            print(pista3)
                            respuesta = input('→ ')
                        else:
                            print('\n')
                            print('Ya viste todas las pistas: ')
                            print(pista1)
                            print(pista2)
                            print(pista3)
                            respuesta = input('→ ')
                    else:
                        respuesta = input('→ ')








    # if eleccion == 'adivinanza1':
    #     adivinanza1 = questions[0]
    #     pregunta1 = adivinanza1["question"]
    #     respuesta1 = adivinanza1["answers"]   #es una lista
    #     pista1 = adivinanza1["clue_1"]
    #     pista2 = adivinanza1["clue_2"]
    #     pista3 = adivinanza1["clue_3"]
    #     print("Pregunta: {} ".format(pregunta1))
    #     respuesta = input('→ ')
    #     while not respuesta.isalpha:
    #         print('Ingresaste datos invalidos, intentalo otra vez')
    #         respuesta = input('→ ')
    #     while True:
    #         if respuesta in respuesta1:
    #             aciertos = aciertos + 1
    #             print('¡Tu respuesta es correcta!')
    #             print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos y usaste {p} pistas.")
    #             os.system('clear')
    #             break
    #         else:
    #             intentos = intentos + 1
    #             aciertos = 0
    #             print('Tu respuesta es incorrecta')
    #             pistas = input('¿Quieres usar una pista?(s/n): ')
    #             while not (pistas=='s' or pistas=='n'):
    #                 print('Ingresaste datos invalidos, intentalo otra vez')
    #                 pistas = input('¿Quieres usar una pista?(s/n): ')

    #             if pistas == 's':
    #                 if intentos == 2:           #si usas una pista se sume
    #                     p = p + 1
    #                     print('\n')
    #                     print(pista1)
    #                     respuesta = input('→ ')
    #                 elif intentos == 3:
    #                     p = p + 1
    #                     print('\n')
    #                     print(pista2)
    #                     respuesta = input('→ ')
    #                 elif intentos == 4:
    #                     p = p + 1
    #                     print('\n')
    #                     print(pista3)
    #                     respuesta = input('→ ')
    #                 else:
    #                     print('\n')
    #                     print('Ya viste todas las pistas: ')
    #                     print(pista1)
    #                     print(pista2)
    #                     print(pista3)
    #                     respuesta = input('→ ')
    #             else:
    #                 respuesta = input('→ ')
    
    # elif eleccion == 'adivinanza2':
    #     adivinanza2 = questions[1]
    #     pregunta2 = adivinanza2["question"]
    #     respuesta2 = adivinanza2["answers"]   #es una lista
    #     pista1 = adivinanza2["clue_1"]
    #     pista2 = adivinanza2["clue_2"]
    #     pista3 = adivinanza2["clue_3"]
    #     print("Pregunta: {} ".format(pregunta2))
    #     respuesta = input('→ ')
    #     while not respuesta.isalpha:
    #         print('Ingresaste datos invalidos, intentalo otra vez')
    #         respuesta = input('→ ')
    #     while True:
    #         if respuesta in respuesta2:
    #             aciertos = aciertos + 1
    #             print('¡Tu respuesta es correcta!')
    #             print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos y usaste {p} pistas.")
    #             os.system('clear')
    #             break
    #         else:
    #             intentos = intentos + 1
    #             aciertos = 0
    #             print('Tu respuesta es incorrecta')
    #             pistas = input('¿Quieres usar una pista?(s/n): ')
    #             while not (pistas=='s' or pistas=='n'):
    #                 print('Ingresaste datos invalidos, intentalo otra vez')
    #                 pistas = input('¿Quieres usar una pista?(s/n): ')
    #             if pistas == 's':
    #                 if intentos == 2:
    #                     p = p + 1
    #                     print('\n')
    #                     print(pista1)
    #                     respuesta = input('→ ')
    #                 elif intentos == 3:
    #                     p = p + 1
    #                     print('\n')
    #                     print(pista2)
    #                     respuesta = input('→ ')
    #                 elif intentos == 4:
    #                     p = p + 1
    #                     print('\n')
    #                     print(pista3)
    #                     respuesta = input('→ ')
    #                 else:
    #                     print('\n')
    #                     print('Ya viste todas las pistas: ')
    #                     print(pista1)
    #                     print(pista2)
    #                     print(pista3)
    #                     respuesta = input('→ ')
    #             else:
    #                 respuesta = input('→ ')
    
    # elif eleccion == 'adivinanza3':
    #     adivinanza3 = questions[2]
    #     pregunta3 = adivinanza3["question"]
    #     respuesta3 = adivinanza3["answers"]   #es una lista
    #     pista1 = adivinanza3["clue_1"]
    #     pista2 = adivinanza3["clue_2"]
    #     pista3 = adivinanza3["clue_3"]
    #     print("Pregunta: {} ".format(pregunta3))
    #     respuesta = input('→ ')
    #     while not respuesta.isalpha:
    #         print('Ingresaste datos invalidos, intentalo otra vez')
    #         respuesta = input('→ ')
    #     while True:
    #         if respuesta in respuesta3:
    #             aciertos = aciertos + 1
    #             print('¡Tu respuesta es correcta!')
    #             print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos y usaste {p} pistas.")
    #             os.system('clear')
    #             break
    #         else:
    #             intentos = intentos + 1
    #             aciertos = 0
    #             print('Tu respuesta es incorrecta')
    #             pistas = input('¿Quieres usar una pista?(s/n): ')
    #             while not (pistas=='s' or pistas=='n'):
    #                 print('Ingresaste datos invalidos, intentalo otra vez')
    #                 pistas = input('¿Quieres usar una pista?(s/n): ')
    #             if pistas == 's':
    #                 if intentos == 2:
    #                     print('\n')
    #                     p = p + 1
    #                     print(pista1)
    #                     respuesta = input('→ ')
    #                 elif intentos == 3:
    #                     print('\n')
    #                     p = p + 1
    #                     print(pista2)
    #                     respuesta = input('→ ')
    #                 elif intentos == 4:
    #                     print('\n')
    #                     p = p + 1
    #                     print(pista3)
    #                     respuesta = input('→ ')
    #                 else:
    #                     print('\n')
    #                     print('Ya viste todas las pistas: ')
    #                     print(pista1)
    #                     print(pista2)
    #                     print(pista3)
    #                     respuesta = input('→ ')
    #             else:
    #                 respuesta = input('→ ')
    