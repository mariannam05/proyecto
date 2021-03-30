from api import *
from random import randrange, choice


eleccion = choice(["quizizz1", "quizizz2", "quizizz3"])
intentos = 1
aciertos = 0
p = 0 #son pistas
questions = datos_quizizz

if eleccion == 'quizizz1':
    quizizz1 = questions[0]
    pregunta1 = quizizz1["question"]
    respuesta1_correcta = quizizz1["correct_answer"]  
    respuesta1_inc1 = quizizz1["answer_2"]  
    respuesta1_inc2 = quizizz1["answer_3"]  
    respuesta1_inc3 = quizizz1["answer_4"]  
    pista1 = quizizz1["clue_1"] 
    print(f'''
    Pregunta: {pregunta1}
    opciones:
    a) {respuesta1_correcta}            b) {respuesta1_inc1}
    c) {respuesta1_inc2}            d) {respuesta1_inc3}
    ''')
    respuesta = input('(a/b/c/d)→ ')
    while not (respuesta=='a' or respuesta=='b' or respuesta=='c' or respuesta=='d'):
        print('Ingresaste datos invalidos, intentalo otra vez')
        respuesta = input('→ ')
    while True:
        if respuesta== 'a':
            aciertos = aciertos + 1
            print('¡Tu respuesta es correcta!')
            print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
            break
        else:
            intentos = intentos + 1
            aciertos = 0
            print('Tu respuesta es incorrecta')
            pistas = input('¿Quieres usar una pista?(s/n): ')
            if pistas == 's':
                p = p + 1
                print(pista1)
                respuesta = input('→ ')
            else:
                respuesta = input('→ ')
elif eleccion == 'quizizz2':
    quizizz2 = questions[1]
    pregunta2 = quizizz2["question"]
    respuesta2_correcta = quizizz2["correct_answer"]  
    respuesta2_inc1 = quizizz2["answer_2"]  
    respuesta2_inc2 = quizizz2["answer_3"]  
    respuesta2_inc3 = quizizz2["answer_4"]  
    pista2 = quizizz2["clue_1"] 
    print(f'''
    Pregunta: {pregunta2}
    opciones:
    a) {respuesta2_inc3}            b) {respuesta2_inc1}
    c) {respuesta2_inc2}            d) {respuesta2_correcta}
    ''')
    respuesta = input('(a/b/c/d)→ ')
    while not (respuesta=='a' or respuesta=='b' or respuesta=='c' or respuesta=='d'):
        print('Ingresaste datos invalidos, intentalo otra vez')
        respuesta = input('→ ')
    while True:
        if respuesta== 'd':
            aciertos = aciertos + 1
            print('¡Tu respuesta es correcta!')
            print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
            break
        else:
            intentos = intentos + 1
            aciertos = 0
            print('Tu respuesta es incorrecta')
            pistas = input('¿Quieres usar una pista?(s/n): ')
            if pistas == 's':
                p = p + 1
                print(pista2)
                respuesta = input('→ ')
            else:
                respuesta = input('→ ')
elif eleccion == 'quizizz3':
    quizizz3 = questions[2]
    pregunta3 = quizizz3["question"]
    respuesta3_correcta = quizizz3["correct_answer"]  
    respuesta3_inc1 = quizizz3["answer_2"]  
    respuesta3_inc2 = quizizz3["answer_3"]  
    respuesta3_inc3 = quizizz3["answer_4"]  
    pista3 = quizizz3["clue_1"] 
    print(f'''
    Pregunta: {pregunta3}
    opciones:
    a) {respuesta3_inc3}        b) {respuesta3_correcta}
    c) {respuesta3_inc2}            d) {respuesta3_inc1}
    ''')
    respuesta = input('(a/b/c/d)→ ').lower()
    while not (respuesta=='a' or respuesta=='b' or respuesta=='c' or respuesta=='d'):
        print('Ingresaste datos invalidos, intentalo otra vez')
        respuesta = input('→ ')
    while True:
        if respuesta== 'b':
            aciertos = aciertos + 1
            print('¡Tu respuesta es correcta!')
            print (f"Felicitaciones! Adivinaste la respuesta en {intentos} intentos y usaste {p} pistas.")
            break
        else:
            intentos = intentos + 1
            aciertos = 0
            print('Tu respuesta es incorrecta')
            pistas = input('¿Quieres usar una pista?(s/n): ')
            if pistas == 's':
                p = p + 1
                print(pista3)
                respuesta = input('→ ')
            else:
                respuesta = input('→ ')
