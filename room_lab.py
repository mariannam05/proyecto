import imagenes
import os
import mensajes
from Cuartos import Cuartos
from Laboratorio import Laboratorio

#datos de ubicacion de la biblioteca con herencia 
obj_izq= 'computadora 1'
obj_der = 'computadora 2'
obj_cen = 'pizarra'
ubi = 0
game = 3
lab = Laboratorio(obj_izq, obj_der, obj_cen, ubi, game)



def func_lab(nuevo_jugador):
    doorClosed = True
    lab = Laboratorio(obj_izq, obj_der, obj_cen, ubi, game)
    print(lab.mostrar())
    
    while doorClosed:
        print(imagenes.laboratorio)
        print(mensajes.comandos)
        seleccion = input(mensajes.direccion).lower()
        while not (seleccion == 'l' or seleccion == 'c' or seleccion == 'r'):
                    print('Lo que ingresaste en esta sala no es válido, asi que elige otra opción')
                    seleccion = input(mensajes.direccion).lower()
        os.system('clear')
        if seleccion == 'r':
            while True:
                print(imagenes.computadora2)
                seleccion = input('Mira! tienes la computadora 2 y necesita una contraseña para ingresar, si introduces la contraseña podras entrar al juego; escribe (ENTER) para regresar:').lower() #idea que se me acaba de ocurrir poner F para regresar solo debemos poner que si escribe F break y clear
                # while not (seleccion == 'r' or seleccion == 'l'):  #aqui hay que validar para todos los otros numeros, letras y enter
                #     seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                contraseña = input('ingrese una contraseña: ')
                os.system('clear')
                break
        elif seleccion == 'l':
            while True:
                print(imagenes.computadora1)
                seleccion = input('Mira! tienes la computadora 1 y necesita un cable HDMI, si lo tienes podras entrar al juego; escribe (ENTER) para regresar:').lower()
                # while not (seleccion == 'r' or seleccion == 'l'):  #aqui hay que validar para todos los otros numeros, letras y enter
                #     seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                os.system('clear')
                break
        else:
            while True:
                print(imagenes.pizarra)
                seleccion = input('Aqui solo tienes la pizarra, y tiene un juego! escribe (c) para jugar o (ENTER) para regresar:').lower()  #aqui la seleccion como es solo los libros es para empezar a jugar
                # while not (seleccion == 'c'):  #aqui hay que validar para todos los otros numeros, letras y enter
                #     seleccion = input('En esta sala solo puedes seleccionar el mueble de libros para jugar o regresarte, asi que selecciona una opcion válida: ').lower()
                os.system('clear')
                break
        os.system('clear')


def main():
    jugador = 'luis'
    func_lab(jugador)

main()