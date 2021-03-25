import imagenes
import os
import mensajes


def biblioteca(nuevo_jugador):
    doorClosed = True
    inventory = ""
    
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
                seleccion = input(mensajes.direccion).lower()
                while (seleccion == 'l' or seleccion == 'c' or seleccion == 'r'):
                    print('En esta sala solo te puedes regresar, asi que presiona ENTER')
                    seleccion = input(mensajes.direccion).lower()
                os.system('clear')
                break
        elif seleccion == 'l':
            while True:
                print(imagenes.mueble_sentarse)
                seleccion = input(mensajes.direccion).lower()
                while (seleccion == 'l' or seleccion == 'c' or seleccion == 'r'):
                    print('En esta sala solo te puedes regresar, asi que presiona ENTER')
                    seleccion = input(mensajes.direccion).lower()
                os.system('clear')
                break
        elif seleccion == 'c':
            while True:
                print(imagenes.mueble_libros)
                seleccion = input(direccion).lower()
                while (seleccion == 'l' or seleccion == 'c' or seleccion == 'r'):
                    print('En esta sala solo te puedes regresar, asi que presiona ENTER')
                    seleccion = input(mensajes.direccion).lower()
                os.system('clear')
                break
        else:
            while True:
                print('lo que acabas de ingresar no es válido, intenta otra vez')
                seleccion = input(mensajes.direccion).lower()
                while (seleccion == 'l' or seleccion == 'c' or seleccion == 'r'):
                    print('flag')
                    seleccion = input(mensajes.direccion).lower()
                os.system('clear')
                break
        os.system('clear')


