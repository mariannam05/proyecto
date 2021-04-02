import time
from Biblioteca import *
from Player import *
from Usuario import *
import imagenes 
import os

comandos= '''
presiona los siguientes comandos para moverte:
r = ir a la derecha de la sala (⇨)
l = ir a la izquierda de la sala (⇦)
c = ir al centro de la sala (⇫)
f = regresar a la sala principal (⇳)
'''

direccion = '¿Qué quieres hacer? →'


def func_biblioteca(jugador):
    tiempo_limite = 60
    comenzar_tiempo = time.time() #para comenzar el tiempo

    while True:
        elapsed_time = time.time() - comenzar_tiempo
        mostrar_tiempo= (tiempo_limite - int(elapsed_time))
        tiempo_restante = round(mostrar_tiempo)
        print(f'su tiempo es de {tiempo_restante}')

        obj_izq= 'mueble para sentarse'
        obj_der = 'mueble de libros pequeño'
        obj_cen = 'mueble de biblioteca'
        game = 3
        ubi = 0  
        biblio = Biblioteca(obj_izq,obj_der,obj_cen,ubi, game)

        
        if mostrar_tiempo <= 0:
            print('Oh no, se te agotó el tiempo 😭')
            print('%sGAME OVER%s' %(fg(1), attr(0)))
            jugador_activo = None
            exit()
            break
        print(biblio.mostrar())
        # jugador.mostrar_atri()
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
                    elif seleccion == 'c':
                        os.system('clear')
                        criptograma_game(jugador)            #juego de criptograma
                elif seleccion == 'r':
                    requisito = 'Martillo'
                    print(f'Necesitas tener {requisito} en tu inventario para poder abrir la puerta')
                    if not requisito in jugador.inventario:
                        print('La puerta esta cerrada asi que regresate')
                        seleccion = input('escribe f:')
                        while not seleccion == 'f':
                            seleccion = input('Escribe un caracter válido (f): ')
                        os.system('clear')
                        break
                    else:
                        print(f'¡Perfecto! tienes el {requisito} para romper el candado, puedes entrar al pasillo de los laboratorios')    #en el pasillo de los laboratorios esta el otro juego
                        os.system('clear')
                        func_pasillo_laboratorio(jugador, tiempo_restante)
                elif seleccion == 'f':
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
                    # elif seleccion == 'c':
                    #     os.system('clear')
                    #     #minijuego       #juego de preguntas matemáticas
                elif seleccion == 'l':
                    os.system('clear')
                    func_saman(jugador, tiempo_restante)        #nos movemos al cuartos de Plaza Rectorado
                elif seleccion == 'f':
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
                        ahorcado_game(jugador)          #juego del ahorcado
                else:
                    os.system('clear')
                    break
        os.system('clear')
        
def main():
    jugador = 'luis'

    func_biblioteca(jugador)
        
main()