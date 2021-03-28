

msg_welcome= ('''
¡¡BIENVENIDO AL MEJOR JUEGO DE LA UNIMET!!
''')

msg_option_menu=('''
Aqui ves las opciones de lo que puedes hacer:
    1. Iniciar Partida.
    2. ¿De que trata este juego?
    3. ¡Records!
''')

msg_registrado = ('''
----------------------------------------------------
ok veo que si quieres jugar , ¿Ya estas registrado?:
    1. No, pero quiero comenzar ya mismo
    2.¡Siii! 👍
----------------------------------------------------
''')

despedida = ('''
bueno, hasta luego 😭
''')

instrucciones = ('''%s
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
        › ENTER: regresar a la sala principal (ojo: si estas en una sala principal y pulsas enter no harás nada)
%s''')

narrativa1 = '''
Bienvenido {nuevo_jugador.username}...
Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad
del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco,
para eso tienes {tiempo_según_dificultad} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto? (s/n) →
'''

comandos= '''
presiona los siguientes comandos para moverte:
r = ir a la derecha de la sala
l = ir a la izquierda de la sala
c = ir al centro de la sala
ENTER: regresar a la sala principal
'''

direccion = '¿Qué quieres hacer? →'

msg_registro1 = '''
----------------------------------------------
Vamos a registrarte para comenzar la aventura:
----------------------------------------------
'''