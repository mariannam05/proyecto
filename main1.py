from mensajes import *
from imagenes import *
import os
from Player import *
from Usuario import  *
from Gandhi import *
from Pelusa import *
from EugenioMendoza import *
from Samanexcentrico import *
from Scharifker import *
from Funciones import *
from colored import fg, bg, attr
import time
from game import *

jugadores = []      #lista para guardar a los jugadores cuando se registren

jugadores = recibir_datos_del_txt('jugadores.txt', jugadores)       #para guardar los usuarios registrados para siempre en la base de datos

#el documento de player.txt lo cree para probarlo ya en el momento final con los usuarios vacios

print('%s¡¡BIENVENIDO AL MEJOR JUEGO DE LA UNIMET!! %s' % (fg(3), attr(0)))     #inicio del juego
while True:
    print(('''
Aqui ves las opciones de lo que puedes hacer:
    1. Iniciar Partida.
    2. ¿De que trata este juego?
    3. ¡Records!
'''))
    menu = input('Ahora cuentame, ¿Qué quieres hacer?: \n ==> ')        #validar aqui
    while (menu != '1' and menu != '2' and menu != '3'):
        print('No seas asi, ingresa una opcion válida 🙄 : ')
        menu = input('¿Qué quieres hacer? (1/2/3): \n ==> ')
    
    if int(menu) == 1:
        #inicio de la partida pero primero registro y verificacion
        print('''
----------------------------------------------------
ok veo que si quieres jugar , ¿Ya estas registrado?:
    1. No, pero quiero comenzar ya mismo
    2.¡Siii! 👍
----------------------------------------------------
''')
        opc= input('==> ')
        while (opc != '1' and opc != '2'):
            print('No seas asi, ingresa una opcion válida 🙄 : ')
            opc= input('==> ')
        if int(opc) == 1:
            print('''
----------------------------------------------
Vamos a registrarte para comenzar la aventura:
----------------------------------------------
''')
            jugadores = registro_jugador(jugadores)
            cargar_datos_en_txt('jugadores.txt', jugadores)
            jugador_activo = jugadores[-1]

        elif int(opc) ==2:
            # verificar que si este registrado
            if len(jugadores) == 0:
                print("Todavía no hay jugadores registrados.")
            else:
                jugador_activo = buscar_jugador(jugadores)

        while jugador_activo != None:
            dificultad = elige_dificultad()
            playtime = selec_tiempo(dificultad)
            vidas = selec_vida(dificultad)
            pistas = selec_pistas(dificultad)
            inventario = []
            tiempo = None
            win = False
            
            jugador = Usuario(jugador_activo.username, jugador_activo.contraseña, jugador_activo.edad, jugador_activo.avatar, pistas, vidas, tiempo, win, inventario, dificultad)
            #primera narrativa
            print(f'''
            Bienvenido {jugador.username}...
            Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad
            del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco,
            para eso cuentas con una cierta cantidad de tiempo antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto? (s/n)
            ''')
            reto = input('→ ')
            while not (reto == 's' or reto == 'n'):
                reto = input("%sPor favor ingrese un valor válido (s/n): %s"% (fg(1), attr(0)))

            while reto == 'n':
                reto = input("No te creo, asi que esperare que lo razones bien y digas que si (vamos por favor, es por una buena causa): ")
            
            #comienza el juego
            #comienza el tiempo
            tiempo_limite = playtime * 60
            comenzar_tiempo = time.time() #para comenzar el tiempo
            fin_tiempo = comenzar_tiempo + tiempo_limite

            while True:
                tiempo_past = time.time() - comenzar_tiempo
                tiempo_restante = round((tiempo_limite - tiempo_past)/60)

                if  int(jugador.vidas) <= 0:
                    print('Oh no, te quedaste sin vidas 😭')            #revisar el por que si pierdo todas las vidas no se detiene el juego
                    print('%sGAME OVER%s' %(fg(1), attr(0)))
                    jugador_activo = None
                    break

                elif time.time() > fin_tiempo:
                    print('Oh no, se te agotó el tiempo 😭')
                    print('%sGAME OVER%s' %(fg(1), attr(0)))
                    jugador_activo = None
                    break
                
                #segunda narrativa
                print(f'''
                Bienvenido {jugador.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, 
                revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.
                ''')
                play(jugador, tiempo_restante)      #revisar por que no se va descontando el tiempo


    elif int(menu)== 2:
        print('\n')
        print('------------------------')
        print('%sEste es un juego muy simple, te explico: %s' % (fg(103), attr(2)))
        print(('''%s
        El juego consiste en que estas en la biblioteca de la UNIMET en cuarentena, para resolver un problema que te contaremos más adelante,
        ahi te debes ir moviendo por las diferentes habitaciones, ir resolviendo acertijos y asi recibir bonificaciones que te ayudaran a resolver
        el problema que te hizo ir hasta la universidad en plena pandemia. 

        IMPORTANTE: 
            El tiempo que tendrás para resolver todos los acertijos dependerá de la dificultad de juego que elijas (fácil, medio, dificil)

        ¿Cómo te mueves en el mapa?
            Sencillo, como cualquier juego de computadora puedes usar las teclas del teclado, los cuales son:
                › r = seleccionar el objeto de la derecha de la sala
                › l = seleccionar el objeto de la izquierda de la sala
                › c = seleccionar el objeto del centro de la sala
                › f: regresar a la sala principal (ojo: si estas en una sala principal y pulsas enter no harás nada)
        %s''') % (fg(109), attr(0)))
        print('------------------------')
        
    # elif int(menu)==3:
    #     records
    otro = input("%s\n¿Desea volver al menu?('S' para 'sí', 'N' para 'no'): %s"% (fg(222), attr(0)))
    while (otro.upper() != 'S') and (otro.upper() != 'N'):
        otro = input("%sPor favor ingrese un valor válido: %s"% (fg(1), attr(0)))
    if otro.upper() == "S":
        continue
    else:
        break
