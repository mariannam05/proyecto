import mensajes
import imagenes
import os
from Player import *
from Gandhi import *
from Pelusa import *
from EugenioMendoza import *
from Samanexcentrico import *
from Scharifker import *



def registro_jugador(jugadores):
    '''
    Con esta función se toman los datos de los nuevos jugadores para registrarlos en la base de datos del juego.

    Argumentos => jugadores: lista de jugadores ya registrados.

    Retorna: => lista "jugadores" con el nuevo jugador agregado a ella.

    '''


    username = input("Ingrese su nombre de usuario: ")

    contraseña = input("Ingrese su nueva contraseña (sin espacios, maximo 10 caracteres): ")
    while (len(contraseña) > 10):
        contraseña = input("Por favor ingrese una contraseña con menos digitos: ")
    
    edad = input('Por favor ingrese su edad: ')
    while not edad.isnumeric():
        edad = input('Por favor ingrese solo numeros: ')
    
    print('''\n
    ---Avatares Disponibles---
        1. Scharifker
        2. Eugenio Mendoza
        3. Pelusa
        4. Gandhi
        5. Samanexcentrico
    ''')

    avatar = input("Introduzca el número correspondiente al avatar que desea utilizar (1-5): ")
    while not (avatar.isnumeric() and int(avatar) in range(1,6)) :
        avatar=input('Por favor introduzca un caracter válido (1-5): ')

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
    print("\n¡Jugador registrado con éxito!\n")
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

def main():

    jugadores = []
    print(mensajes.msg_welcome)

    while True:
        print(mensajes.msg_option_menu)
        menu = input('Ahora cuentame, ¿Qué quieres hacer?: \n ==> ')
        while (int(menu) not in range(1,4)) and (not menu.isnumeric()):
            print('No seas asi, ingresa una opcion válida 🙄 : ')
        

        if int(menu) == 1:
            print(mensajes.msg_registrado)
            opc= input('==> ')
            while (int(opc) not in range(1,3)) and (not opc.isnumeric()):
                print('No seas asi, ingresa una opcion válida 🙄 : ')

            if int(opc) == 1:
                print(mensajes.msg_registro1)
                registro_jugador(jugadores)
                print('\n')
                # comenzar_juego(jugadores)
                # AQUI ES DONDE DEBES VERIFICAR Y HACER UNA FUNCION LLAMADA DIFICULTAD donde DECIDES ESO

            elif int(opc) ==2:
                # verificar que si este registrado
                if len(jugadores) == 0:
                    print("Todavía no hay jugadores registrados.")
                else:
                    buscar_jugador(jugadores)

        elif int(menu)== 2:
            print(mensajes.instrucciones)

        otro = input("\n¿Desea volver al menu?('S' para 'sí', 'N' para 'no'): ")
        os.system('clear')
        while (otro.upper() != 'S') and (otro.upper() != 'N'):
            otro = input("Por favor ingrese un valor válido: ")
        if otro.upper() == "S":
            continue
        else:
            break

main()