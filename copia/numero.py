from api import *
import os
from random import randrange, choice
from colored import fg, bg, attr

import random


intentos = 0
p = 0 #pistas
n = random.randint(1, 15)
game = juego_numeros
quiz = game['questions']
recompensa = game['award']
pregunta = quiz[0]
p1 = pregunta['question']
print(p1) 
numerosadivinados = []
while True:
    print('Intenta adivinar.') 
    num = input('==> ')
    while not (num == '1' or num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9' or num == '10' or num == '11' or num == '12' or num == '13' or num == '14' or num == '15'):
        print('Ingresaste datos invalidos, intentalo otra vez')
        num = input('==> ')

    intentos = intentos + 1
    if num in numerosadivinados:
        print('Ya ingresaste ese numero, intentalo otra vez')
        num = input('==> ')

    if intentos == 3:
        print('\n')
        #quitar un cuarto de vida
        print('ya llevas 3 intentos, te quito un cuarto de tu vida')
    elif intentos == 6:
        print('\n')
        #quitar un cuarto de vida
        print('ya llevas 6 intentos, te quito otro cuarto de tu vida')
    elif intentos == 9:
        print('\n')
        #quitar un cuarto de vida
        print('ya llevas 9 intentos, te quito otro cuarto de tu vida')
    elif intentos == 12:
        print('\n')
        #quitar un cuarto de vida
        print('ya llevas 12 intentos, te quito otro cuarto de tu vida')

    if int(num) == n:
        print('\n')
        print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
        print(f'Haz ganado un {recompensa}, lo puedes ver en tu inventario!')
        # jugador.agregar_inv(recompensa)
        salida = input('Escribe (f) para regresar: ')
        while not salida == 'f':
            salida = input('Por favor, escribe (f) para regresar: ')
        os.system('clear')
        break

    if jugador.pistas == 0:
            print('No tienes mas pistas, sigue intentando tu solo...')
            num = input('==> ')
    else:
        pistas = input('¿Quieres usar una pista?(s/n): ')
        while not (pistas=='s' or pistas=='n'):
            print('Ingresaste datos invalidos, intentalo otra vez')
            pistas = input('¿Quieres usar una pista?(s/n): ')
        if pistas == 's':
            p = p + 1
            print('menos una pista')
            # jugador.pistas = jugador.pistas - 1
            if int(num) < n:
                numerosadivinados.append(num)
                print('Estas por debajo del numero.') # Hay ocho espacios delante de print.
            if int(num) > n:
                numerosadivinados.append(num)
                print('Estas por arriba del numero.')
        else:
            continue
