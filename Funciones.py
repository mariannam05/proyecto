import mensajes
import imagenes
import os
from Player import *
from Gandhi import *
from Pelusa import *
from EugenioMendoza import *
from Samanexcentrico import *
from Scharifker import *
from colored import fg, bg, attr
import pickle
import os


def registro_jugador(jugadores):
    '''
    Con esta función se toman los datos de los nuevos jugadores para registrarlos en la base de datos del juego.

    Argumentos => jugadores: lista de jugadores ya registrados.

    Retorna: => lista "jugadores" con el nuevo jugador agregado a ella.

    '''


    username = input("%sIngrese su nombre de usuario: %s"% (fg(51), attr(0)))

    contraseña = input("%sIngrese su nueva contraseña (sin espacios, maximo 10 caracteres): %s"% (fg(51), attr(0)))
    while (len(contraseña) > 10):
        contraseña = input("%sPor favor ingrese una contraseña con menos digitos: %s"% (fg(1), attr(0)))
    
    edad = input('%sPor favor ingrese su edad: %s'% (fg(51), attr(0)))
    while not edad.isnumeric():
        edad = input('%sPor favor ingrese solo numeros: %s'% (fg(1), attr(0)))
    
    print('''%s\n
    ---Avatares Disponibles---
        1. Scharifker
        2. Eugenio Mendoza
        3. Pelusa
        4. Gandhi
        5. Samanexcentrico
    %s'''% (fg(141), attr(0)))

    avatar = input("%sIntroduzca el número correspondiente al avatar que desea utilizar (1-5): %s"% (fg(51), attr(0)))
    while not (avatar.isnumeric() and int(avatar) in range(1,6)) :
        avatar=input('%sPor favor introduzca un caracter válido (1-5): %s'% (fg(1), attr(0)))

    if int(avatar) == 1:
        avatar = "Scharifker"

    elif int(avatar) == 2:
        avatar = "Eugenio Mendoza"

    elif int(avatar) == 3:
        avatar = "Pelusa"

    elif int(avatar) == 4:
        avatar = "Gandhi"

    elif int(avatar) == 5:
        avatar = "Samanexcentrico"

    nuevo_jugador  = Player(username, contraseña, edad, avatar)
    jugadores.append(nuevo_jugador)
    print("\n%s¡Jugador registrado con éxito!\n%s"% (fg(10), attr(0)))
    nuevo_jugador.mostrar()

    return jugadores


# def ver_jugadores(jugadores):
#     '''
#     Con esta función se le aplica a todos los jugadores el método "mostrar" para imprimir de forma organizada sus atributos.

#     Argumentos => jugadores: lista de jugadores ya registrados.

#     Retorna: => para cada jugador se imprime el número de registro y seguidamente sus datos.

#     '''
#     for i,a in enumerate(jugadores):
#         print("---",i+1,"---------------")
#         a.mostrar()


def buscar_jugador(jugadores):
    '''
    Con esta función verificamos si el jugador esta registrado o no en la base de datos, haciendo que ingresen el username y comprobado la contraseña.

    Argumentos => jugadores: lista de jugadores ya registrados.

    Retorna: => si el username ingresado esta registrado o no.

    '''
    j = input('Ingresa tu username: ')
    for a in jugadores:
        if a.username == j:
            print(f'{j} si esta registrado!')
            clave = input('ingrese su contraseña: ')
            while not (clave == a.contraseña):
                clave = input('CONTRASEÑA INCORRECTA, ingrese la contraseña nuevamente: ')
            if a.contraseña == clave:
                print(f'perfecto, si eres tu {j}!')
                return j
    print(f'El username {j}, no esta registrado todavía 🥴')
    


def recibir_datos_del_txt(nombre_txt,datos):
    
    lectura_binaria= open(nombre_txt,'rb')
    
    if os.stat(nombre_txt).st_size != 0:
        datos=pickle.load(lectura_binaria)

    lectura_binaria.close()

    return datos



def cargar_datos_en_txt(nombre_txt,datos):

    escritura_binaria=open(nombre_txt,'wb')

    datos=pickle.dump(datos,escritura_binaria)
    
    escritura_binaria.close()
    

def elige_dificultad():
    print("""
    ¿Preparado?
    Elige la dificultad  en la que quieres jugar:
    1. Fácil (relajado)
    2. Medio (si te sientes con suerte)
    3. Dificil (solo para expertos)
    """)
    opcion = input("=> ")
    while not (opcion==1 or opcion==2 or opcion==3):
        opcion = input("%sPor favor ingrese un valor válido (1/2/3): %s"% (fg(1), attr(0)))
    
    if opcion == 1:
        opcion = 'facil'
    elif opcion == 2:
        opcion = 'medio'
    elif opcion == 3:
        opcion = 'dificil'

    return opcion 

def selec_tiempo(dificultad):
    with open('dificultad.txt', 'r') as d:
        for line in d:
            if line.split(',')[0] == dificultad:
                tiempo = line.split(',')[1]
                tiempo = tiempo.replace(' ', '')
                tiempo = tiempo.replace('minutos', '')
                return int(tiempo)

def selec_vida(dificultad):
    with open('dificultad.txt', 'r') as d:
        for line in d:
            if line.split(',')[0] == dificultad:
                vida = line.split(',')[2]
                vida = vida.replace(' ', '')
                vida = vida.replace('vidas', '')
                if int(vida)==0:
                    return 1

                return int(vida)

def selec_pistas(dificultad):
    with open('dificultad.txt', 'r') as d:
        for line in d:
            if line.split(',')[0] == dificultad:
                pistas = line.split(',')[3]
                pistas = pistas.replace(' ', '')
                pistas = pistas.replace('pistas', '')
                return int(pistas)
