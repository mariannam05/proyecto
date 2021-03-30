#api
# import requests
# url = "https://api-escapamet.vercel.app/"
# response = requests.get(url)
# info_rooms = response.json()

questions=[
{
"question": "Soy alta cuando soy joven y baja cuando soy vieja. ¿Qué soy yo?",
"answers": ["una vela","vela","Vela","la Vela","La Vela"],
"clue_1": "lo usas cuando se va la luz",
"clue_2": "lo puedes prender con un encendedor",
"clue_3": "es de cera"
},
{
"question": "Es pequeño como una pera, pero alumbra la casa entera. ¿Qué soy yo?",
"answers": ["un bombillo","bombillo","El Bombillo","el bombillo","Bombillo"],
"clue_1": "lo usas cuando hay luz",
"clue_2": "gracias a estar encendido puedes leer",
"clue_3": "se coloca en las lámparas"
},
{
"question": "Oro parece y plata no es, y no lo adivinas de aquí a un mes ¿Qué soy yo?",
"answers": ["un platano","platano","El Platano","Platano","plátano","Plátano"],
"clue_1": "fruta",
"clue_2": "POTASIO",
"clue_3": "parecido al cambur"
}]

from random import randrange, choice

eleccion = choice(["adivinanza1", "adivinanza2", "adivinanza3"])
intentos = 1
aciertos = 0
p = 0 #cant de pistas usadas
if eleccion == 'adivinanza1':
    adivinanza1 = questions[0]
    pregunta1 = adivinanza1["question"]
    respuesta1 = adivinanza1["answers"]   #es una lista
    pista1 = adivinanza1["clue_1"]
    pista2 = adivinanza1["clue_2"]
    pista3 = adivinanza1["clue_3"]
    print("Pregunta: {} ".format(pregunta1))
    respuesta = input('→ ')
    while not respuesta.isalpha:
        print('Ingresaste datos invalidos, intentalo otra vez')
        respuesta = input('→ ')
    while True:
        if respuesta in respuesta1:
            aciertos = aciertos + 1
            print('¡Tu respuesta es correcta!')
            print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos y usaste {p} pistas.")
            break
        else:
            intentos = intentos + 1
            aciertos = 0
            print('Tu respuesta es incorrecta')
            pistas = input('¿Quieres usar una pista?(s/n): ')
            if pistas == 's':
                if intentos == 2:           #si usas una pista se sume
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

elif eleccion == 'adivinanza2':
    adivinanza2 = questions[1]
    pregunta2 = adivinanza2["question"]
    respuesta2 = adivinanza2["answers"]   #es una lista
    pista1 = adivinanza2["clue_1"]
    pista2 = adivinanza2["clue_2"]
    pista3 = adivinanza2["clue_3"]
    print("Pregunta: {} ".format(pregunta2))
    respuesta = input('→ ')
    while not respuesta.isalpha:
        print('Ingresaste datos invalidos, intentalo otra vez')
        respuesta = input('→ ')
    while True:
        if respuesta in respuesta2:
            aciertos = aciertos + 1
            print('¡Tu respuesta es correcta!')
            print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos y usaste {p} pistas.")
            break
        else:
            intentos = intentos + 1
            aciertos = 0
            print('Tu respuesta es incorrecta')
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

elif eleccion == 'adivinanza3':
    adivinanza3 = questions[2]
    pregunta3 = adivinanza3["question"]
    respuesta3 = adivinanza3["answers"]   #es una lista
    pista1 = adivinanza3["clue_1"]
    pista2 = adivinanza3["clue_2"]
    pista3 = adivinanza3["clue_3"]
    print("Pregunta: {} ".format(pregunta3))
    respuesta = input('→ ')
    while not respuesta.isalpha:
        print('Ingresaste datos invalidos, intentalo otra vez')
        respuesta = input('→ ')
    while True:
        if respuesta in respuesta3:
            aciertos = aciertos + 1
            print('¡Tu respuesta es correcta!')
            print (f"Felicitaciones! Adivinaste la palabra en {intentos} intentos y usaste {p} pistas.")
            break
        else:
            intentos = intentos + 1
            aciertos = 0
            print('Tu respuesta es incorrecta')
            pistas = input('¿Quieres usar una pista?(s/n): ')
            if pistas == 's':
                if intentos == 2:
                    print('\n')
                    p = p + 1
                    print(pista1)
                    respuesta = input('→ ')
                elif intentos == 3:
                    print('\n')
                    p = p + 1
                    print(pista2)
                    respuesta = input('→ ')
                elif intentos == 4:
                    print('\n')
                    p = p + 1
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
