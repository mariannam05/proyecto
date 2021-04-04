import imagenes
import os
from Cuarto import Cuarto
from Biblioteca import Biblioteca
from Servidores import Servidores
from Laboratorio import Laboratorio
from Saman import Saman
from api import *
from random import randrange, choice
from main1 import *
from Juego import *
from Quizizz import *
from Criptograma import *
from Sopa_de_Letras import *
from Ahorcado import *
from Emoji import *
from Adivinanza import *
from Logica import *
from Numero import *
from Python import *
from Mezclada import *
from Matematica import *
from Pelicula import *
from Memoria import *
from colored import fg, bg, attr


#mensajes
comandos= '''
presiona los siguientes comandos para moverte:
r = ir a la derecha de la sala (⇨)
l = ir a la izquierda de la sala (⇦)
c = ir al centro de la sala (⇫)
f = regresar a la sala principal (⇳)
'''

comandos_saman ='''
presiona los siguientes comandos para moverte:
r = ir a la derecha de la sala (⇨)
l = ir a la izquierda de la sala (⇦)
c = ir al centro de la sala (⇫)
b = si quieres volver a la biblioteca (⇳)
'''

comandos_lab ='''
presiona los siguientes comandos para moverte:
r = ir a la computadora 2 (⇨)
l = ir a la computadora 1 (⇦)
c = ir al centro de la sala (⇫)
a = si quieres volver al pasillo (⇳)
s = si quieres ir al cuarto de servidores (⇳)
'''

comandos_serv ='''
presiona los siguientes comandos para moverte:
r = ir a la papelera (⇨)
l = ir al Rack (⇦)
c = ir al centro de la sala (⇫)
a = si quieres volver al laboratorio (⇳)
'''
comandos_puerta ='''
presiona los siguientes comandos para moverte:
a = si quieres ir a los laboratorios (⇨)
b = si quieres volver a la biblioteca (⇦)
c = jugar (⇫)
f = regresar (⇳)
'''
direccion = '¿Qué quieres hacer? →'

def ganador_final(jugador, tiempo_restante):
    #ultima narrativa
    print(f'''%s%s
    ¡¡Ganaste el juego!!
        ¡Felicidades! Has logrado evitar una catástrofe en la Unimet, pero te das cuenta que todo esto fue un sueño no?        
        Seguimos en cuarentena y no puedes ir a la universidad. ¡Así que levántate rápido que tienes una clase en zoom en media hora!              %s'''% (fg(0), bg(222), attr(0)))

    return exit()

def func_servidores(jugador, tiempo_restante):
    obj_izq= 'Rack'
    obj_der = 'papelera'
    obj_cen = 'puerta'
    ubi = 0
    game = 3
    serv = Servidores(obj_izq, obj_der, obj_cen, ubi, game)
    while jugador.vidas > 0:
        print(serv.mostrar())
        jugador.mostrar_atri()
        print(f'Su tiempo restante es {tiempo_restante} minutos!')
        print(imagenes.servidores)
        print(comandos_serv)
        seleccion = input(direccion).lower()
        while not (seleccion == 'l' or seleccion == 'c' or seleccion == 'r' or seleccion == 'a'):
                    print('Lo que ingresaste en esta sala no es válido, asi que elige otra opción')
                    seleccion = input(direccion).lower()
        os.system('clear')

        if seleccion == 'r':
            while True:
                print(imagenes.papelera)
                seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ')
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('Por favor selecciona una opcion válida (c/f): ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                elif seleccion == 'c':
                    premio = 'título Universitario'
                    if premio in jugador.inventario:            #validamos que no juegue 2 veces
                        print('Ya reclamaste este premio, regresate')
                        salida = input('Escribe (f) para regresar: ')
                        while not salida == 'f':
                            salida = input('Por favor, escribe (f) para regresar: ')
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        game = juego_numeros
                        name = game['name']
                        recompensa = game['award']
                        reglas = game['rules']
                        position = posicion_num
                        cuarto = nombre_num
                        a = Numero(name, reglas, recompensa, position, cuarto)        #Clase Numeros
                        a.mostrar_cuarto()
                        a.mostrar()       
                        a.numero_game(jugador)         #juego de numero al azar
                           
        elif seleccion == 'l':
            while True:
                print(imagenes.rack)
                seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ')
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('Por favor selecciona una opcion válida (c/f): ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                elif seleccion == 'c':
                    premio = "contraseña"
                    if premio in jugador.inventario:            #validamos que no juegue 2 veces
                        print("Ya reclamaste este premio, no puedes jugar más")
                        salida = input('Escribe (f) para regresar: ')
                        while not salida == 'f':
                            salida = input('Por favor, escribe (f) para regresar: ')
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        game = juego_mezclada
                        name = game['name']
                        recompensa = game['award']
                        reglas = game['rules']
                        position = posicion_mezclada
                        cuarto = nombre_mezclada
                        s = Mezclada(name, reglas, recompensa, position, cuarto)          #Clase Mezclada
                        s.mostrar_cuarto()
                        s.mostrar()       
                        s.mezclada_game(jugador)        #juego de Palabra mezclada

        elif seleccion == 'c':
            while True:
                print(imagenes.puerta_salida)
                seleccion = input('Aqui solo tienes la puerta de salida, y tiene un juego! escribe (c) para jugar o (f) para regresar:').lower()  
                while not (seleccion == 'c' or seleccion == 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble de libros para jugar o regresarte, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'c':
                    requisito = ['carnet','Disco Duro']
                    r1 = "carnet" 
                    r2 = "Disco Duro"
                    print(f'Debes tener un {requisito} para poder jugar este juego')
                    if not r1 and r2 in jugador.inventario:
                        print(f'No tienes el {requisito} en tu inventario, asi que debes regresarte a conseguirlo')
                        seleccion = input('escribe (f):')
                        while not seleccion == 'f':
                            seleccion = input('Escribe un caracter válido (f): ')
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        game = juego_final
                        name = 'Adivina la pelicula con emojis'
                        recompensa = game['award']
                        reglas = game['rules']
                        position = posicion_final
                        cuarto = nombre_final
                        s = Pelicula(name, reglas, recompensa, position, cuarto)          #Clase Peliculas
                        s.mostrar_cuarto()
                        s.mostrar()       
                        s.peliculas_game(jugador)     #juego de libre (adivina la pelicula con emojis)
                        ganador_final(jugador, tiempo_restante)

                elif seleccion == 'f':
                    os.system('clear')
                    break

        elif seleccion == 'a':
            os.system('clear')
            func_lab(jugador, tiempo_restante)
        os.system('clear')

def func_lab(jugador, tiempo_restante):
    #datos de ubicacion del laboratorio 
    obj_izq= 'computadora 1'
    obj_der = 'computadora 2'
    obj_cen = 'pizarra'
    ubi = 0
    game = 3
    lab = Laboratorio(obj_izq, obj_der, obj_cen, ubi, game)
    while jugador.vidas > 0:
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
                        premio = 'llave'
                        if premio in jugador.inventario:            #validamos que no juegue 2 veces
                            print('Ya reclamaste este premio, regresate')
                            salida = input('Escribe (f) para regresar: ')
                            while not salida == 'f':
                                salida = input('Por favor, escribe (f) para regresar: ')
                            os.system('clear')
                            break
                        else:
                            os.system('clear')
                            game = juego_adivinanzas
                            name = game['name']
                            recompensa = game['award']
                            reglas = game['rules']
                            position = posicion_adivinanzas
                            cuarto = nombre_adivinanzas
                            d = Adivinanza(name, reglas, recompensa, position, cuarto)      #Clase Adivinanzas
                            d.mostrar_cuarto()
                            d.mostrar()       
                            d.adivinanzas_game(jugador)  #juego de adivinanzas
                        
                         
                           
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
                        premio = 'carnet'
                        if premio in jugador.inventario:            #validamos que no juegue 2 veces
                            print('Ya reclamaste este premio, regresate')
                            salida = input('Escribe (f) para regresar: ')
                            while not salida == 'f':
                                salida = input('Por favor, escribe (f) para regresar: ')
                            os.system('clear')
                            break
                        else:
                            os.system('clear')
                            game = juego_python
                            name = game['name']
                            recompensa = game['award']
                            reglas = game['rules']
                            position = posicion_python
                            cuarto = nombre_python
                            l = Python(name, reglas, recompensa, position, cuarto)      #Clase Python
                            l.mostrar_cuarto()
                            l.mostrar()       
                            l.python_game(jugador)   #juego de Preguntas sobre python

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
                        premio = "Vida Extra Sopa"
                        if premio in jugador.inventario:            #validamos que no juegue 2 veces
                            print("Ya reclamaste esta vida extra, no puedes jugar más")
                            salida = input('Escribe (f) para regresar: ')
                            while not salida == 'f':
                                salida = input('Por favor, escribe (f) para regresar: ')
                            os.system('clear')
                            break
                        else:
                            os.system('clear')
                            game = juego_sopa
                            name = game['name']
                            recompensa = game['award']
                            reglas = game['rules']
                            position = posicion_sopa
                            cuarto = nombre_sopa
                            s = Sopa_de_letras(name, reglas, recompensa, position, cuarto)          #Clase Sopa de letras
                            s.mostrar_cuarto()
                            s.mostrar()       
                            s.sopa_game(jugador)          #juego de sopa  de letras
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

def func_pasillo_laboratorio(jugador, tiempo_restante):     
    while jugador.vidas > 0:
        print('''
    Nombre del cuarto: Pasillo laboratorio
        ''')
        jugador.mostrar_atri()
        print(f'Su tiempo restante es {tiempo_restante} minutos!')
        print(imagenes.puerta_laboratorio)
        print(comandos_puerta)
        seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar, (f) para regresar, (a) para avanzar a los laboratorios o (b) para volver a la biblioteca: ')
        while not (seleccion == 'c' or seleccion== 'f' or seleccion== 'a' or seleccion== 'b'):  
            seleccion = input('Por favor selecciona una opcion válida (c/f/a/b): ').lower()
        if seleccion == 'f':
            os.system('clear')
            break
        elif seleccion == 'c':
            while True:
                premio = 'libro de Física'
                if premio in jugador.inventario:            #validamos que no juegue 2 veces
                    print('Ya reclamaste este premio, regresate')
                    salida = input('Escribe (f) para regresar: ')
                    while not salida == 'f':
                        salida = input('Por favor, escribe (f) para regresar: ')
                    os.system('clear')
                    break
                else:
                    os.system('clear')
                    game = juego_booleana
                    name = game['name']
                    recompensa = game['award']
                    reglas = game['rules']
                    position = posicion_booleana
                    cuarto = nombre_booleana
                    l = Logica(name, reglas, recompensa, position, cuarto)      #Clase Logica
                    l.mostrar_cuarto()
                    l.mostrar()       
                    l.logica_booleana_game(jugador) #juego de logica booleana

        elif seleccion == 'a':
            os.system('clear')
            func_lab(jugador, tiempo_restante) 
        elif seleccion == 'b':
            os.system('clear')
            func_biblioteca(jugador, tiempo_restante) 


def func_saman(jugador, tiempo_restante):
    obj_izq= 'Banco para sentarse 1'
    obj_der = 'Banco para sentarse 2'
    obj_cen = 'Saman'
    game = 3
    ubi = 0
    sam = Saman(obj_izq,obj_der,obj_cen,ubi, game)
    
    while jugador.vidas > 0:
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
                    premio = 'martillo'
                    if premio in jugador.inventario:            #validamos que no juegue 2 veces
                        print('Ya reclamaste este premio, regresate')
                        salida = input('Escribe (f) para regresar: ')
                        while not salida == 'f':
                            salida = input('Por favor, escribe (f) para regresar: ')
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        game = juego_memoria
                        name = game['name']
                        recompensa = game['award']
                        reglas = game['rules']
                        position = posicion_memoria
                        cuarto = nombre_memoria
                        x = Memoria(name, reglas, recompensa, position, cuarto)         #Clase Mmemoria
                        x.mostrar_cuarto()
                        x.mostrar()       
                        x.memoria_game(jugador)     #juego de memoria
                    
        elif seleccion == 'l':
            while True:
                print(imagenes.banco)
                seleccion = input('este parece ser un banquito común, pero hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ').lower()
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                elif seleccion == 'c':
                    premio = 'libro de matemáticas'
                    if premio in jugador.inventario:            #validamos que no juegue 2 veces
                        print('Ya reclamaste este premio, regresate')
                        salida = input('Escribe (f) para regresar: ')
                        while not salida == 'f':
                            salida = input('Por favor, escribe (f) para regresar: ')
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        game = juego_quizizz
                        name = game['name']
                        recompensa = premio
                        reglas = game['rules']
                        position = posicion_quizizz
                        cuarto = nombre_quizizz
                        x = Quizizz(name, reglas, recompensa, position, cuarto)         #Clase Quizizz
                        x.mostrar_cuarto()
                        x.mostrar()       
                        x.game_q(jugador)  #juego de quizizz
                    
        elif seleccion == 'c':
            while True:
                print(imagenes.saman)
                seleccion = input('Aqui esta frente a ti el famoso saman de la unimet y tiene algo especial... Hay un juego aqui!, escribe (c) si quieres jugar o (f) para regresar: ').lower()
                while not (seleccion == 'c' or seleccion== 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble, la puerta o regresar, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'f':
                    os.system('clear')
                    break
                elif seleccion == 'c':
                    os.system('clear')
                    r_mostrar = ["Titulo Universitario","Mensaje"]
                    r1 = "título Universitario" 
                    r2 = "Mensaje: Si estas gradudado puedes pisar el Samán"
                    print(f'Necesitas tener {r_mostrar} en tu inventario')

                    if not r1 and r2 in jugador.inventario:
                        print('Pierdes una vida porque no tienes todos los requisitos para jugar este juego')
                        jugador.quitar_vidas(1)
                    else:
                        premio = 'Disco Duro'
                        if premio in jugador.inventario:            #validamos que no juegue 2 veces
                            print('Ya reclamaste este premio, regresate')
                            salida = input('Escribe (f) para regresar: ')
                            while not salida == 'f':
                                salida = input('Por favor, escribe (f) para regresar: ')
                            os.system('clear')
                            break
                        else:
                            os.system('clear')
                            game = juego_dibujos
                            name = game['name']
                            recompensa = game['award']
                            reglas = game['rules']
                            position = posicion_dibujos
                            cuarto = nombre_dibujos
                            e = Emoji(name, reglas, recompensa, position, cuarto)        #clase Emojis
                            e.mostrar_cuarto()
                            e.mostrar()       
                            e.emojis_game(jugador)        #juego de logica con emojis
                    
        else: 
            func_biblioteca(jugador, tiempo_restante)
        os.system('clear')


def func_biblioteca(jugador, tiempo_restante):
    obj_izq= 0
    obj_der = 0
    obj_cen = 0
    game = 3
    ubi = 0  
    biblio = Biblioteca(obj_izq,obj_der,obj_cen,ubi, game)
    
    while jugador.vidas > 0:
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
                    elif seleccion == 'c':
                        requisito = 'llave'
                        if not requisito in jugador.inventario:
                            print(f'No me puedes abrir, busca algo para abrirme')
                            print('todavia no tienes en tu inventario el objeto que necesito para abrirme, ve y consiguelo!')
                            seleccion = input('escribe f:')
                            while not seleccion == 'f':
                                seleccion = input('Escribe un caracter válido (f): ')
                            os.system('clear')
                            break
                        else:
                            premio = 'Mensaje: Si estas gradudado puedes pisar el Samán'
                            if premio in jugador.inventario:                #validamos que no juegue 2 veces
                                print('Ya reclamaste este premio, regresate')
                                salida = input('Escribe (f) para regresar: ')
                                while not salida == 'f':
                                    salida = input('Por favor, escribe (f) para regresar: ')
                                os.system('clear')
                                break
                            else:
                                os.system('clear')
                                game = juego_criptograma
                                name = game['name']
                                recompensa = premio
                                reglas = game['rules']
                                position = posicion_criptograma
                                cuarto = nombre_criptograma
                                c = Criptograma(name, reglas, recompensa, position, cuarto)         #Clase Criptograma
                                c.mostrar_cuarto()
                                c.mostrar()       
                                c.criptograma_game(jugador)            #juego de criptograma

                elif seleccion == 'r':
                    requisito = 'martillo'
                    if not requisito in jugador.inventario:
                        print(f'Necesitas tener {requisito} en tu inventario para poder abrir la puerta')
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
                    elif seleccion == 'c':
                        requisito = 'libro de matemáticas'
                        if not requisito in jugador.inventario:
                            print('Necesito que sepas derivar')
                            print('todavia no tienes en tu inventario el objeto que necesito, ve y consiguelo!')
                            seleccion = input('escribe f:')
                            while not seleccion == 'f':
                                seleccion = input('Escribe un caracter válido (f): ')
                            os.system('clear')
                            break
                        else:
                            premio = 'Vida Extra Mate'
                            if premio in jugador.inventario:                #validamos que no juegue 2 veces
                                print('Ya reclamaste este premio, regresate')
                                salida = input('Escribe (f) para regresar: ')
                                while not salida == 'f':
                                    salida = input('Por favor, escribe (f) para regresar: ')
                                os.system('clear')
                                break
                            else:
                                os.system('clear')
                                game = juego_mate
                                name = game['name']
                                recompensa = game['award']
                                reglas = game['rules']
                                position = posicion_mate
                                cuarto = nombre_mate
                                c = Matematica(name, reglas, recompensa, position, cuarto)         #Clase Matematica
                                c.mostrar_cuarto()
                                c.mostrar()       
                                c.mate_game(jugador)            #juego de preguntas matemáticas


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
                        premio = 'cable HDMI'       #validamos que no juegue 2 veces
                        if premio in jugador.inventario:
                            print('Ya reclamaste este premio, regresate')
                            salida = input('Escribe (f) para regresar: ')
                            while not salida == 'f':
                                salida = input('Por favor, escribe (f) para regresar: ')
                            os.system('clear')
                            break
                        else:
                            os.system('clear')
                            game = juego_ahorcado
                            name = game['name']
                            recompensa = game['award']
                            reglas = game['rules']
                            position = posicion_ahorcado
                            cuarto = nombre_ahorcado
                            a = Ahorcado(name, reglas, recompensa, position, cuarto)        #Clase Ahorcado
                            a.mostrar_cuarto()
                            a.mostrar()       
                            a.ahorcado_game(jugador)          #juego del ahorcado
                else:
                    os.system('clear')
                    break
        os.system('clear')


def play(jugador, tiempo_restante):
    func_biblioteca(jugador, tiempo_restante)
    