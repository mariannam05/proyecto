def func_servidores(jugador, tiempo_restante):
    obj_izq= 'Rack'
    obj_der = 'papelera'
    obj_cen = 'puerta'
    ubi = 0
    game = 3
    serv = servidores(obj_izq, obj_der, obj_cen, ubi, game)
    while True:
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
                    os.system('clear')
                    #inicio del minijuego   #juego de Palabra mezclada
                           
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
                        #inicio del minijuego   #juego de Palabra mezclada

        elif seleccion == 'c':
            while True:
                print(imagenes.puerta_salida)
                seleccion = input('Aqui solo tienes la puerta de salida, y tiene un juego! escribe (c) para jugar o (f) para regresar:').lower()  
                while not (seleccion == 'c' or seleccion == 'f'):  
                    seleccion = input('En esta sala solo puedes seleccionar el mueble de libros para jugar o regresarte, asi que selecciona una opcion válida: ').lower()
                if seleccion == 'c':
                    requisito = 'carnet'
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
                        #inicio del minijuego   #juego de libre #Parar el cronómetro y ganar el juego   #si pierdes, vas perdiendo una vida completa
                elif seleccion == 'f':
                    os.system('clear')
                    break

        elif seleccion == 'a':
            os.system('clear')
            func_lab(jugador, tiempo_restante)
        os.system('clear')