import imagenes
import os
import mensajes
from Cuartos import Cuartos
from Laboratorio import Laboratorio

 

def func_lab(jugador, tiempo_restante):
    #datos de ubicacion del laboratorio 
    obj_izq= 'computadora 1'
    obj_der = 'computadora 2'
    obj_cen = 'pizarra'
    ubi = 0
    game = 3
    lab = Laboratorio(obj_izq, obj_der, obj_cen, ubi, game)
    while True:
        print(lab.mostrar())
        jugador.mostrar_atri()
        print(f'Su tiempo restante es {tiempo_restante} minutos!')
        print(imagenes.laboratorio)
        print(comandos_lab)
        seleccion = input(direccion).lower()
        while not (seleccion == 'l' or seleccion == 'c' or seleccion == 'r' or seleccion == 'a' or seleccion == 's'):
                    print('Lo que ingresaste en esta sala no es válido, asi que elige otra opción')
                    seleccion = input(direccion).lower()
        os.system('clear')

        if seleccion == 'r':
            while True:
                print(imagenes.computadora2)
                seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ')
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('Por favor selecciona una opcion válida (c/f): ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                elif seleccion == 'c':
                    print('Debes tener la contraseña:')
                    contraseña = input('''
                    Ingrese la contraseña aqui: ''')
                    if not contraseña == 'contraseña':
                        print("%sContraseña Incorrecta: %s"% (fg(1), attr(0)))
                        seleccion = input('escribe (f) para regresarte e intentarlo nuevamente:')
                        while not seleccion == 'f':
                            seleccion = input('Escribe un caracter válido (f): ')
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        adivinanzas_game(jugador)   #juego de logica booleana#inicio del minijuego
                           
        elif seleccion == 'l':
            while True:
                print(imagenes.computadora1)
                seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ')
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('Por favor selecciona una opcion válida (c/f): ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                elif seleccion == 'c':
                    requisito = 'cable HDMI'
                    print(f'Debes tener un {requisito} para poder jugar este juego')
                    if not requisito in jugador.inventario:
                        print(f'No tienes el {requisito} en tu inventario, asi que debes regresarte a conseguirlo')
                        seleccion = input('escribe (f):')
                        while not seleccion == 'f':
                            seleccion = input('Escribe un caracter válido (f): ')
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        #inicio del minijuego   #juego de Preguntas sobre python

        elif seleccion == 'c':
            while True:
                print(imagenes.pizarra)
                seleccion = input('Aqui solo tienes la pizarra, y tiene un juego! escribe (c) para jugar o (f) para regresar:').lower()  
                while not (seleccion == 'c' or seleccion == 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble de libros para jugar o regresarte, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'c':
                    seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ')
                    while not (seleccion == 'c' or seleccion== 'f'):  
                        seleccion = input('Por favor selecciona una opcion válida (c/f): ').lower()
                    if seleccion == 'f':
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        #inicio del minijuego          #juego de sopa  de letras
                else:
                    os.system('clear')
                    break
        elif seleccion == 'a':
            os.system('clear')
            func_pasillo_laboratorio(jugador, tiempo_restante)

        elif seleccion == 's':
            os.system('clear')
            func_servidores(jugador, tiempo_restante)
        os.system('clear')