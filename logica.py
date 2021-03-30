from api import *
from random import randrange, choice
#funcion de juego de logica booleana que esta en el pasillo de los laboratorios
def logica_booleana_game():
    eleccion = choice(["p1", "p2"])
    intentos = 1
    aciertos = 0
    questions = datos_logica

    if eleccion == 'p1':
        p1 = questions[0]
        pregunta1 = p1['question']
        respuesta1 = p1['answer']
        print(f'''
    Pregunta: {pregunta1}
    Respuesta: ''')
        respuesta = input('→ ')
        while not respuesta.isalpha:
            print('Ingresaste datos invalidos, intentalo otra vez')
            respuesta = input('→ ')

        while True:
            if respuesta == respuesta1:
                aciertos = aciertos + 1
                print('\n')
                print('¡Tu respuesta es correcta!')
                print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos.")
                break
            else:
                intentos = intentos + 1
                aciertos = 0
                print('\n')
                print('Tu respuesta es incorrecta')
                respuesta = input('→ ')
    elif eleccion == 'p2':
        p2 = questions[1]
        pregunta2 = p2['question']
        respuesta2 = p2['answer']
        print(f'''
    Pregunta: {pregunta2}
    Respuesta: ''')
        respuesta = input('→ ')
        while not respuesta.isalpha:
            print('Ingresaste datos invalidos, intentalo otra vez')
            respuesta = input('→ ')

        while True:
            if respuesta == respuesta2:
                aciertos = aciertos + 1
                print('\n')
                print('¡Tu respuesta es correcta!')
                print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos.")
                break
            else:
                intentos = intentos + 1
                aciertos = 0
                print('\n')
                print('Tu respuesta es incorrecta, recuerda el buen uso de las mayusculas en la lógica!')
                respuesta = input('→ ')




