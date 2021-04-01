# import random
# def crear_matriz(num):
#     matriz = []
#     a = 0
#     for i in range(6):
#         matriz.append([])
#         for j in range(6):
#             matriz[i].append(num[a])
#             a += 1
#     for i in range(len(matriz)):
#         print(matriz[i])
#     return matriz

# def crear_tablero():
#     tablero = [
#         ["_","_","_","_","_","_"],
#         ["_","_","_","_","_","_"],
#         ["_","_","_","_","_","_"],
#         ["_","_","_","_","_","_"],
#         ["_","_","_","_","_","_"],
#         ["_","_","_","_","_","_"]]
    
#     for i in tablero:
#         for j in i:
#             print(j, " ", end="")
#         print()
#     return tablero

# def mostrar(a,b,tablero,matriz):
#     tablero[b-1][a-1]=matriz[a-1][b-1]
#     for i in tablero:
#         for j in i:
#             print(j, " ", end="")
#         print()
#     return tablero[b-1][a-1]

# def limpiar(a1, b1, a2, b2):
#     tablero[b1-1][a1-1] = "_"
#     tablero[b2-1][a2-1] = "_"
#     for i in tablero:
#         for j in i:
#             print(j, " ", end="")
#         print()

# def cambio_jugador(jugador):
#     if jugador==1:
#         jugador == 2
#     else:
#         jugador == 1
#     return jugador

# def validar(a,b,a2,b2):
#     if a<1 or a>6 or b<1 or b>6 or tablero[b-1][a-1] != "_":
#         print("Carta Invalida")
#         return False
#     elif a==a2 and b==b2:
#         print("Esa carta ya fue usada")
#         return False
#     else:
#         return True

# def sumar_puntos(puntos):
#     puntos += 1
#     return puntos

# def winner (puntos1, puntos2):
#     if puntos1 > puntos2:
#         print(f"El jugador 1 ha ganado {puntos1} puntos")
#         ganador= True
#     elif puntos2 > puntos1:
#         print(f"El jugador 2 ha ganado {puntos2} puntos")
#         ganador= True
#     else:
#         print("Hubo empate")
#         ganador= True
#     return ganador

# def ver_mov():
#     guiones = 0
#     for i in tablero:
#         for j in i:
#             if j =="_":
#                 guiones += 1
#     return guiones

# numeros = []
# print("Empieza el jugeo de memoria")
# for i in range(1,19):
#     numeros.append(i)
#     numeros.append(i)
# random.shuffle(numeros)
# matriz = crear_matriz(numeros)
# tablero= crear_tablero()
# jugando = True
# jugador = 1
# puntos1 = 0
# puntos2 = 0
# ganador = False
# guiones = 0
# while jugando == True and ganador == False:
#     seguir = False
#     print(f"sigue el jugador {jugador}")
#     valido1 = False
#     valido2 = False
#     while valido1 == False:
#         a1= int(input("carta en a del primer numero: "))
#         b1= int(input("carta en b del primer numero: "))
#         valido1 = validar(a1, b1, -1, -1)
#     print(f"Agarraste {matriz[a1-1][b1-1]}")
#     while valido2 == False:
#         a2= int(input("carta en a del primer numero: "))
#         b2= int(input("carta en b del primer numero: "))
#         valido1 = validar(a2, b2, -1, -1)
#     print(f"Agarraste {matriz[a2-1][b2-1]}")
#     tabla1 = mostrar(a1,b1,tablero, matriz)
#     print("primer numero")
#     tabla2 = mostrar(a2,b2,tablero, matriz)
#     print("segundo numero")
#     if tabla1 == tabla2:
#         print("Esta bien")
#         if jugador == 1:
#             puntos1 = sumar_puntos(puntos1)
#         else:
#             puntos2 = sumar_puntos(puntos2)
#         seguir = True
#     else:
#         print("esta mal")
#         limpiar(a1,b1,a2,b2)
#     if ver_mov()==0 and ganador==False:
#         ganador = winner(puntos1, puntos2)
#         seguir = True
#     while seguir == False:
#         resp = input ("¿Quieres seguir?(s/n): ")
#         if resp == 's':
#             jugando = True
#             jugador = cambio_jugador(jugador)
#             seguir = True
#         elif resp == 'n':
#             jugando = False
#             print(f"puntos finales de jugador 1: {puntos1}")
#             print(f"puntos finales de jugador 2: {puntos2}")
#             winner(puntos1,puntos2)
#             seguir= True
#         else:
#             seguir = False





# import random, sys
 
# seguir = "s" or "S"
# while seguir == "s" or "S":
 
#     #cartes = [1, 2, 3, 4, 5, 6, 11, 12, 14, 15]
#     cartes = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
 
#     parejas = len(cartes)
 
#     tiradas = 0
 
#     # Cargamos la lista
#     taulell = []
#     for i in range(2):
#         taulell.append([])
#         for j in range(4):
#             taulell[i].append([])
#             for k in range(5):
#                 taulell[i][j].append('?')
 
#     # Duplicamos las cartas
#     cartes = cartes*2
 
#     # Barajamos las cartas
#     random.shuffle(cartes)
 
#     # Cargamos la capa 0 (la capa que no se muestra) con las cartas
#     k = 0
#     for i in range(4):
#         for j in range(5):
#             taulell[0][i][j] = chr(cartes[k])
#             k = k + 1
 
#     # Mostramos la capa 1 y las coordenadas
#     def mostrar_tablero(tablero):
#         sys.stdout.write(' |')
#         for x in range(5):
#             sys.stdout.write(' ' + str(x))
#         sys.stdout.write('\n')
#         print ("============")
#         lletra = 'A'
#         for i in range(4):
#             sys.stdout.write(lletra+'|')
#             lletra = chr(ord(lletra) + 1)
#             for j in range(5):
#                 sys.stdout.write(' ' + taulell[1][i][j])
#             sys.stdout.write('\n')
 
#     mostrar_tablero(taulell)
#     while taulell[1] != taulell[0]:
#         fila = input("Fila?")
#         fila = ord(fila) - 65
#         columna = int(input("Columna?"))
 
#         while columna > 4 or columna < 0 or fila > 4 or fila < 0:
#             print ("Valor incorrecto")
#             fila = input("Fila?")
#             fila = ord(fila) - 65
#             columna = int(input("Columna?"))
 
#         taulell[1][fila][columna] = taulell[0][fila][columna]
#         mostrar_tablero(taulell)
 
#         resultado_1 = taulell[1][fila][columna]
 
#         fila_auxiliar = input("Fila?")
#         fila_auxiliar = ord(fila_auxiliar) - 65
#         columna_auxiliar = int(input("Columna?"))
 
#         while columna_auxiliar > 4 or columna_auxiliar < 0 or fila_auxiliar > 4 or fila_auxiliar < 0:
#             print ("Valor incorrecto")
#             fila_auxiliar = input("Fila?")
#             fila_auxiliar = ord(fila_auxiliar) - 65
#             columna_auxiliar = int(input("Columna?"))
 
#         taulell[1][fila_auxiliar][columna_auxiliar] = taulell[0][fila_auxiliar][columna_auxiliar]
#         mostrar_tablero(taulell)
#         resultado_2 = taulell[1][fila_auxiliar][columna_auxiliar]
 
#         tiradas += 1
 
#         if resultado_1 != resultado_2:
#             taulell[1][fila][columna] = "?"
#             taulell[1][fila_auxiliar][columna_auxiliar] = "?"
#         else:
#             parejas -= 1
#             print ("Correcto, te quedan ", parejas, " parejas")
 
#     print ("Has necesitado ", tiradas, " tiradas")
#     seguir = input("Quieres seguir jugando?")
#     seguir.lower()
 
 
 
# input()










































# import os

# questions=[
# {
# "question": "[['😀', '🙄', '🤮', '🥰'],\n['🤮', '😨', '🤓', '😷'],\n['😨', '🤓', '🥰', '😷'],\n['🤑', '🤑', '🙄', '😀']]",
# "clue_1": "Decirte donde está escondida una que levantes"
# }
# ]

# question1 = questions[0]
# pregunta1 = question1["question"]  #es una lista de listas
# pista1 = question1["clue_1"]
# c1 = pregunta1[3]
# c2 = pregunta1[8]
# c3 = pregunta1[13]
# c4 = pregunta1[18]
# c5 = pregunta1[25]
# c6 = pregunta1[30]
# c7 = pregunta1[35]
# c8 = pregunta1[40]

# c9 = pregunta1[47]
# c10 = pregunta1[52]
# c11 = pregunta1[57]
# c12 = pregunta1[62]
# c13 = pregunta1[69]
# c14 = pregunta1[74]
# c15 = pregunta1[79]
# c16 = pregunta1[84]

# respuestas = ['listo', 'Listo', 'l', 'L']

# print('Comienza el juego, memoriza la posicion de las cartas: ')
# print(f'''
#                     {c1} {c2} {c3} {c4}
#                     {c5} {c6} {c7} {c8}
#                     {c9} {c10} {c11} {c12}
#                     {c13} {c14} {c15} {c16}
# ''')
# comienza = input('Escribe (listo / l) para comenzar: ')
# while not comienza in respuestas:
#     print('Lo que escribiste no es válido, intentalo nuevamente')
#     comienza = input('Escribe (listo / l) para comenzar: ')
# os.system('clear')
# while True:
#     print('''
#     Encuentrame!
#                         1   2   3   4
#                         5   6   7   8
#                         9   10  11  12
#                         13  14  15  16
#     ''')
#     escribe = input('Escribe el numero de la carta que quieres ver: (1/16) ')
#     while not (escribe.isnumeric() or int(escribe) not in range(1,17)):
#         print('Lo que escribiste no es válido, intentalo nuevamente')
#         escribe = input('Escribe el numero de la carta que quieres ver:(1/16) ')

#     if int(escribe) == 1:
#         print(f'''
#                        {c1}   2   3   4
#                         5   6   7   8
#                         9   10  11  12
#                         13  14  15  16
#     ''')
#         escribe = input('Escribe el numero de la otra carta que quieres ver: (2/16) ')
#         while not (escribe.isnumeric() or int(escribe) not in range(2,17) or int(escribe)==1):
#             print('Lo que escribiste no es válido, intentalo nuevamente')
#             escribe = input('Escribe el numero de la carta que quieres ver:(1/16) ')
        
#         if int(escribe)==16:
#             tablero1 = (f'''
#     Encontraste una pareja!!
#                         {c1}   2   3   4
#                         5   6   7   8
#                         9   10  11  12
#                         13  14  15  {c16}
#             ''')
#             print(tablero1)
#             # encontrado1 == True
#             continue
#         elif int(escribe)==2:
#             print(f'''
#             No es una pareja :(
#                            {c1}   {c2}   3   4
#                             5   6   7   8
#                             9   10  11  12
#                             13  14  15  16
#             ''')
#     if int(escribe) == 2:
#         # if encontrado1 == True:           #continuar con el juego despues
#             print(tablero1)
#             escribe = input('Escribe el numero de la otra carta que quieres ver: (1/16) ')
#             # while not (escribe.isnumeric() or int(escribe) not in range(1,17)):
#             #     print('Lo que escribiste no es válido, intentalo nuevamente')
#             #     escribe = input('Escribe el numero de la carta que quieres ver:(1/16) ')


    
    
    
    
#     break







# grid = [[[' X', '😀'],[' X', '🙄'],[' X', '🤮'],[' X', '🥰']],
#         [[' X', '🤮'],[' X', '😨'],[' X', '🤓'],[' X', '😷']],
#         [[' X', '😨'],[' X', '🤓'],[' X', '🥰'],[' X', '😷']],
#         [[' X', '🤑'],[' X', '🤑'],[' X', '🙄'],[' X', '😀']]]

# fila1= grid[0]
# lista1 = fila1[0]
# print(lista1)
