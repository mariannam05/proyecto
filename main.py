from Funciones import *
from mensajes import *
from imagenes import *
import os

print(mensajes.msg_welcome)
jugadores = []
while True:
    print(mensajes.msg_option_menu)
    menu = input('Ahora cuentame, ¿Qué quieres hacer?: \n ==> ')
    while (int(menu) not in range(1,4)) and (not menu.isnumeric()):
        print('No seas asi, ingresa una opcion válida 🙄 : ')
    
    if int(menu)== 1:
        print(mensajes.msg_registrado)
        opc= input('==> ')
        while (int(opc) not in range(1,3)) and (not opc.isnumeric()):
            print('No seas asi, ingresa una opcion válida 🙄 : ')

        if int(opc) == 1:
            print('\n')
            print('Vamos a registrarte para comenzar la aventura:')
            registrar_jugador(jugadores)
            print('\n')
            # comenzar_juego(jugadores)
            # AQUI ES DONDE DEBES VERIFICAR Y HACER UNA FUNCION LLAMADA DIFICULTAD donde DECIDES ESO

        elif int(opc) ==2:
            # verificar que si este registrado
            ver_jugadores(jugadores)

    elif int(menu)== 2:
        print(mensajes.instrucciones)

    # elif int(menu)== 3:

    otro = input("\n¿Volvemos al menu? ('S' para 'sí', 'N' para 'no'): ")
    os.system('clear')
    while (otro.upper() != 'S') and (otro.upper() != 'N'):
        otro = input("Por favor ingrese un valor válido: ")
    if otro.upper() == "S":
        continue
    else:
        break


