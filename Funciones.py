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


def ver_jugadores(jugadores):
    '''
    Con esta función se le aplica a todos los jugadores el método "mostrar" para imprimir de forma organizada sus atributos.

    Argumentos => jugadores: lista de jugadores ya registrados.

    Retorna: => para cada jugador se imprime el número de registro y seguidamente sus datos.

    '''
    for i,a in enumerate(jugadores):
        print("---",i+1,"---------------")
        a.mostrar()


def buscar_jugador(jugadores):
    '''
    Con esta función verificamos si el jugador esta registrado o no en la base de datos, haciendo que ingresen el username y comprobado la contraseña.

    Argumentos => jugadores: lista de jugadores ya registrados.

    Retorna: => si el username ingresado esta registrado o no.

    '''
    buscar = input('Ingresa tu username: ')
    for i,a in enumerate(jugadores):
        print("---",i+1,"---------------")
        if a.username == buscar:
            print(f'{buscar} si esta registrado!')
            clave = input('ingrese su contraseña: ')
            while not (clave == a.contraseña):
                clave = input('CONTRASEÑA INCORRECTA, ingrese la contraseña nuevamente: ')
            if a.contraseña == clave:
                print(f'perfecto, si eres tu {buscar}!')
        else:
            print(f'lo sentimos pero {buscar} no esta registrado todavia')




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
    