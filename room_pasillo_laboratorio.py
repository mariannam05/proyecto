def func_pasillo_laboratorio(jugador, tiempo_restante):
    while True:
        print('''
        Nombre del cuarto: Pasillo laboratorio
        ''')
        jugador.mostrar_atri()
        print(f'Su tiempo restante es {tiempo_restante} minutos!')
        print(imagenes.puerta_laboratorio)
        seleccion = input('Hay un juego aqui!, escribe (c) si quieres jugar, (f) para regresar, (a) para avanzar a los laboratorios o (b) para volver a la biblioteca: ')
        while not (seleccion == 'c' or seleccion== 'f' or seleccion== 'a' or seleccion== 'b'):  
            seleccion = input('Por favor selecciona una opcion válida (c/f/a/b): ').lower()
        if seleccion == 'f':
            os.system('clear')
            break
        elif seleccion == 'c':
            os.system('clear')
            logica_game(jugador)   #juego de logica booleana
        elif seleccion == 'a':
            os.system('clear')
            func_lab(jugador, tiempo_restante) 
        elif seleccion == 'b':
            os.system('clear')
            func_biblioteca(jugador, tiempo_restante) 