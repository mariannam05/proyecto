import imagenes
import os
import mensajes
from Cuartos import Cuartos
from Biblioteca import Biblioteca

#datos de ubicacion de la biblioteca con herencia 

obj_izq= 'mueble para sentarse'
obj_der = 'mueble de libros pequeño'
obj_cen = 'mueble de biblioteca'
game = 3
ubi = 0


def func_biblioteca(nuevo_jugador):
    doorClosed = True    
    biblio = Biblioteca(obj_izq,obj_der,obj_cen,ubi, game)
    print(biblio.mostrar())
    
    while doorClosed:
        print(imagenes.biblioteca)
        print(mensajes.comandos)
        seleccion = input(mensajes.direccion).lower()
        while not (seleccion == 'l' or seleccion == 'c' or seleccion == 'r'):
                    print('Lo que ingresaste en esta sala no es válido, asi que elige otra opción')
                    seleccion = input(mensajes.direccion).lower()
        os.system('clear')
        if seleccion == 'r':
            while True:
                print(imagenes.mueble_pequeño)
                seleccion = input('OK tienes el estante pequeño y la puerta que va a los laboratorios, escribe (l) para seleccionar el mueble, (r) para intentar abrir la puerta o (ENTER) para regresar:').lower()
                # while not (seleccion == 'r' or seleccion == 'l'):  #aqui hay que validar para todos los otros numeros, letras y enter
                #     seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                os.system('clear')
                break
        elif seleccion == 'l':
            while True:
                print(imagenes.mueble_sentarse)
                seleccion = input('Aqui tienes el mueble para que tomes una siestica y la puerta que va al saman, escribe (l) para seleccionar el mueble, (r) para intentar abrir la puerta o (ENTER) para regresar:').lower()
                # while not (seleccion == 'r' or seleccion == 'l'):  #aqui hay que validar para todos los otros numeros, letras y enter
                #     seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                os.system('clear')
                break
        else:
            while True:
                print(imagenes.mueble_libros)
                seleccion = input('Aqui solo tienes el mueble de libros, y tiene un juego! escribe (c) para jugar o (ENTER) para regresar:').lower()  #aqui la seleccion como es solo los libros es para empezar a jugar
                # while not (seleccion == 'c'):  #aqui hay que validar para todos los otros numeros, letras y enter
                #     seleccion = input('En esta sala solo puedes seleccionar el mueble de libros para jugar o regresarte, asi que selecciona una opcion válida: ').lower()
                os.system('clear')
                break
        os.system('clear')


def main():
    jugador = 'luis'
    func_biblioteca(jugador)

main()