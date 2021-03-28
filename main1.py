import mensajes
import imagenes
import os
from Player import *
from Gandhi import *
from Pelusa import *
from EugenioMendoza import *
from Samanexcentrico import *
from Scharifker import *
from Funciones import *
from colored import fg, bg, attr



jugadores = []      #lista para guardar a los jugadores cuando se registren

jugadores = recibir_datos_del_txt('jugadores.txt', jugadores)       #para guardar los usuarios registrados para siempre en la base de datos

#api
import requests
url = "https://api-escapamet.vercel.app/"
response = requests.get(url)
info_rooms = response.json()
print(info_rooms)


print('%s¡¡BIENVENIDO AL MEJOR JUEGO DE LA UNIMET!! %s' % (fg(3), attr(0)))     #inicio del juego
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
            jugadores=registro_jugador(jugadores)
            cargar_datos_en_txt('jugadores.txt', jugadores)
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
        print('\n')
        print('------------------------')
        print('%sEste es un juego muy simple, te explico: %s' % (fg(103), attr(2)))
        print((mensajes.instrucciones) % (fg(109), attr(0)))
        print('------------------------')
        
    otro = input("%s\n¿Desea volver al menu?('S' para 'sí', 'N' para 'no'): %s"% (fg(222), attr(0)))
    while (otro.upper() != 'S') and (otro.upper() != 'N'):
        otro = input("%sPor favor ingrese un valor válido: %s"% (fg(1), attr(0)))
    if otro.upper() == "S":
        continue
    else:
        break
