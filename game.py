import imagenes
import os
from mensajes import *
from Cuartos import Cuartos
from Biblioteca import Biblioteca
from Saman import Saman
from room_biblioteca import *
from room_saman import *
from api import *
from random import randrange, choice
from quizizz import *

#mensajes
comandos= '''
presiona los siguientes comandos para moverte:
r = ir a la derecha de la sala
l = ir a la izquierda de la sala
c = ir al centro de la sala
f = regresar a la sala principal
'''

comandos_saman ='''
presiona los siguientes comandos para moverte:
r = ir a la derecha de la sala
l = ir a la izquierda de la sala
c = ir al centro de la sala
b = si quieres volver a la biblioteca
'''

direccion = '¿Qué quieres hacer? →'

def func_saman(jugador, tiempo_restante):
    obj_izq= 'Banco para sentarse 1'
    obj_der = 'Banco para sentarse 2'
    obj_cen = 'Saman'
    game = 3
    ubi = 0
    sam = Saman(obj_izq,obj_der,obj_cen,ubi, game)
    
    while True:
        print(sam.mostrar())
        jugador.mostrar_atri()
        print(f'Su tiempo restante es {tiempo_restante} minutos!')
        print(imagenes.saman)
        print(comandos_saman)
        seleccion = input(direccion).lower()
        while not (seleccion == 'l' or seleccion == 'c' or seleccion == 'r' or seleccion == 'b'):
                    print('Lo que ingresaste en esta sala no es válido, asi que elige otra opción')
                    seleccion = input(direccion).lower()
        os.system('clear')
        if seleccion == 'r':
            while True:
                print(imagenes.banco)
                seleccion = input('este parece ser un banquito común, pero hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ').lower()
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                elif seleccion == 'c':
                    os.system('clear')
                    quizizz_game(jugador)
                    
        elif seleccion == 'l':
            while True:
                print(imagenes.banco)
                seleccion = input('este parece ser un banquito común, pero hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ').lower()
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                # elif seleccion == 'c':
                #     #inicio del minijuego
        elif seleccion == 'c':
            while True:
                print(imagenes.saman)
                seleccion = input('Aqui esta frente a ti el famoso saman de la unimet y tiene algo especial... Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ').lower()
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                # elif seleccion == 'c':
                #     #inicio del minijuego
        else: 
            func_biblioteca(jugador, tiempo_restante)
        os.system('clear')


def func_biblioteca(jugador, tiempo_restante):
    obj_izq= 'mueble para sentarse'
    obj_der = 'mueble de libros pequeño'
    obj_cen = 'mueble de biblioteca'
    game = 3
    ubi = 0
    doorClosed = True    
    biblio = Biblioteca(obj_izq,obj_der,obj_cen,ubi, game)
    
    while doorClosed:
        print(biblio.mostrar())
        jugador.mostrar_atri()
        print(f'Su tiempo restante es {tiempo_restante} minutos!')
        print(imagenes.biblioteca)
        print(comandos)
        seleccion = input(direccion).lower()
        while not (seleccion == 'l' or seleccion == 'c' or seleccion == 'r'):
                    print('Lo que ingresaste en esta sala no es válido, asi que elige otra opción')
                    seleccion = input(direccion).lower()
        os.system('clear')
        if seleccion == 'r':
            while True:
                print(imagenes.mueble_pequeño)
                seleccion = input('OK tienes el estante pequeño y la puerta que va a los laboratorios, escribe (l) para seleccionar el mueble, (r) para intentar abrir la puerta o (f) para regresar:').lower()
                while not (seleccion == 'r' or seleccion == 'l' or seleccion== 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'l':
                    seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ')
                    while not (seleccion == 'c' or seleccion== 'f'):  
                        seleccion = input('Por favor selecciona una opcion válida (c/f): ').lower()
                    if seleccion == 'f':
                        os.system('clear')
                        break
                    # elif seleccion == 'c':
                    #     #inicio del minijuego
                elif seleccion == 'r':
                    #va asi porque todavia  no he creado el inventario con la llave en DoorClosed = True
                    print('La puerta esta cerrada asi que regresate: ')
                    seleccion = input('escribe f:')
                    while not seleccion == 'f':
                        seleccion = input('Escribe un caracter válido: ')
                    os.system('clear')
                    break
                    # else:
                        #cuando ya tiene la llave en su inventario
                else:
                    os.system('clear')
                    break

        elif seleccion == 'l':
            while True:
                print(imagenes.mueble_sentarse)
                seleccion = input('Aqui tienes el mueble para que tomes una siestica y la puerta que va al saman, escribe (r) para seleccionar el mueble, (l) para ir al saman o (f) para regresar:').lower()
                while not (seleccion == 'r' or seleccion == 'l' or seleccion == 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'r':
                    seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ')
                    while not (seleccion == 'c' or seleccion== 'f'):  
                        seleccion = input('Por favor selecciona una opcion válida (c/f): ').lower()
                    if seleccion == 'f':
                        os.system('clear')
                        break
                elif seleccion == 'l':
                    os.system('clear')
                    func_saman(jugador, tiempo_restante)
                else:
                    os.system('clear')
                    break
        else:
            while True:
                print(imagenes.mueble_libros)
                seleccion = input('Aqui solo tienes el mueble de libros, y tiene un juego! escribe (c) para jugar o (f) para regresar:').lower()  
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
                    break
        os.system('clear')


def play(jugador, tiempo_restante):
    func_biblioteca(jugador, tiempo_restante)