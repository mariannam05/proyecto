import os

questions=[
{
"question": "[['😀', '🙄', '🤮', '🥰'],\n['🤮', '😨', '🤓', '😷'],\n['😨', '🤓', '🥰', '😷'],\n['🤑', '🤑', '🙄', '😀']]",
"clue_1": "Decirte donde está escondida una que levantes"
}
]

question1 = questions[0]
pregunta1 = question1["question"]  #es una lista de listas
pista1 = question1["clue_1"]
c1 = pregunta1[3]
c2 = pregunta1[8]
c3 = pregunta1[13]
c4 = pregunta1[18]
c5 = pregunta1[25]
c6 = pregunta1[30]
c7 = pregunta1[35]
c8 = pregunta1[40]

c9 = pregunta1[47]
c10 = pregunta1[52]
c11 = pregunta1[57]
c12 = pregunta1[62]
c13 = pregunta1[69]
c14 = pregunta1[74]
c15 = pregunta1[79]
c16 = pregunta1[84]

respuestas = ['listo', 'Listo', 'l', 'L']

print('Comienza el juego, memoriza la posicion de las cartas: ')
print(f'''
                    {c1} {c2} {c3} {c4}
                    {c5} {c6} {c7} {c8}
                    {c9} {c10} {c11} {c12}
                    {c13} {c14} {c15} {c16}
''')
comienza = input('Escribe (listo / l) para comenzar: ')
while not comienza in respuestas:
    print('Lo que escribiste no es válido, intentalo nuevamente')
    comienza = input('Escribe (listo / l) para comenzar: ')
os.system('clear')
while True:
    print('''
    Encuentrame!
                        1   2   3   4
                        5   6   7   8
                        9   10  11  12
                        13  14  15  16
    ''')
    escribe = input('Escribe el numero de la carta que quieres ver: (1/16) ')
    while not (escribe.isnumeric() or int(escribe) not in range(1,17)):
        print('Lo que escribiste no es válido, intentalo nuevamente')
        escribe = input('Escribe el numero de la carta que quieres ver:(1/16) ')

    if int(escribe) == 1:
        print(f'''
                       {c1}   2   3   4
                        5   6   7   8
                        9   10  11  12
                        13  14  15  16
    ''')
        escribe = input('Escribe el numero de la otra carta que quieres ver: (2/16) ')
        while not (escribe.isnumeric() or int(escribe) not in range(2,17) or int(escribe)==1):
            print('Lo que escribiste no es válido, intentalo nuevamente')
            escribe = input('Escribe el numero de la carta que quieres ver:(1/16) ')
        
        if int(escribe)==16:
            tablero1 = (f'''
    Encontraste una pareja!!
                        {c1}   2   3   4
                        5   6   7   8
                        9   10  11  12
                        13  14  15  {c16}
            ''')
            print(tablero1)
            # encontrado1 == True
            continue
        elif int(escribe)==2:
            print(f'''
            No es una pareja :(
                           {c1}   {c2}   3   4
                            5   6   7   8
                            9   10  11  12
                            13  14  15  16
            ''')
    if int(escribe) == 2:
        # if encontrado1 == True:           #continuar con el juego despues
            print(tablero1)
            escribe = input('Escribe el numero de la otra carta que quieres ver: (1/16) ')
            # while not (escribe.isnumeric() or int(escribe) not in range(1,17)):
            #     print('Lo que escribiste no es válido, intentalo nuevamente')
            #     escribe = input('Escribe el numero de la carta que quieres ver:(1/16) ')


    
    
    
    
    break







# grid = [[[' X', '😀'],[' X', '🙄'],[' X', '🤮'],[' X', '🥰']],
#         [[' X', '🤮'],[' X', '😨'],[' X', '🤓'],[' X', '😷']],
#         [[' X', '😨'],[' X', '🤓'],[' X', '🥰'],[' X', '😷']],
#         [[' X', '🤑'],[' X', '🤑'],[' X', '🙄'],[' X', '😀']]]

# fila1= grid[0]
# lista1 = fila1[0]
# print(lista1)
