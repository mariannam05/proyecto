from api import *
from random import randrange, choice

#funcion de juego de logica booleana que esta en el pasillo de los laboratorios
def logica_booleana_game(jugador):
    '''
    Juego Lógica Booleana
    Recibe: Diccionario del juego y objeto jugador
    Devuelve: True cuando el usuario complete el juego
    '''

    #"message_requirement": "Está cerrado con candado!!!!!",
    #"requirement": "martillo",
    #"name": "Lógica Booleana",
    #"award": "libro de Física",
    #"rules": "pierde media vida por opción incorrecta",
    
    game = juego_booleana
    quiz = choice(game['questions']) #escoge un diccionario de la lista aleatoriamente
    requerido = game['requirement']
    recompensa = game['award']
    reglas = game['rules']

    print(f'Para jugar necesitas tener en tu inventario {requerido}!!')
    print(f'Estas son las reglas del juego: {reglas}')
    print(f'La recomensa de este juego es: {recompensa}')

    pregunta = quiz['question']
    respuesta1 = quiz['answer']
    respuesta2 = lambda x: 'True' if x == 'False' else 'False'

    print(f'''Pregunta: {pregunta}
    
    a) {respuesta2(respuesta1)}
    b) {respuesta1}
    Respuesta:
    ''')
    r = input('(a/b)→ ').lower()
    while r != 'a' and r != 'b':
        print('Ingresaste datos invalidos, intentalo otra vez')
        r = input('(a/b)→ ').lower()
        
    while True:
        if r == 'b':
            print('¡Tu respuesta es correcta!')
            print (f"Felicitaciones! Haz ganado un {recompensa}, lo puedes ver en tu inventario!")
            jugador.agregar_inv(recompensa)
            salida = input('Escribe (f) para regresar: ')
            while not salida == 'f':
                salida = input('Por favor, escribe (f) para regresar: ')
            os.system('clear')
            break

        else:
            print('Tu respuesta es incorrecta')
            jugador.quitar_vidas(1/2)
        





    