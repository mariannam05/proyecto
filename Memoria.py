from api import *
from random import *
import os
from Juego import Juego
from api import *
import os
from random import randrange, choice, sample
from colored import fg, bg, attr

#clase hija de la clase juegos

class Memoria(Juego):
    def __init__(self,name, reglas, recompensa, position, cuarto):
        self.cuarto = cuarto
        super().__init__(name,reglas,recompensa,position)
    
    def mostrar_cuarto(self):
        print(f'Esta en el objeto: {self.cuarto}')

    def memoria_game(self, jugador): 
        game = juego_memoria
        recompensa = game['award']       
        def show_grid(g):
                num = ['     0', '  1', '  2', '  3']
                print('   '.join(num))
                for j, linea in enumerate(g):
                        print(j, linea)
                print('\n')

        s_grid = [
        ['๐','๐','๐คก','๐'],
        ['๐คก','๐จ','๐ค','๐ท'],
        ['๐จ','๐ค','๐','๐ท'],
        ['๐ค','๐ค','๐','๐']
        ]
        grid = []
        e_grid = [
        ['--', '--', '--', '--'],
        ['--', '--', '--', '--'],
        ['--', '--', '--', '--'],
        ['--', '--', '--', '--']
        ]
        for l in s_grid:
                shuffle(l)
                grid.append(l)
        show_grid(grid)
        l = input('Presione cualquier tecla cuando estรฉ listo: ')
        os.system('clear')
        show_grid(e_grid)
        while True:
                x = input('Fila (X): ')
                while not x.isnumeric() or int(x) > (len(grid)-1):
                    print('Ingreso invรกlido')
                    x = input('Fila (X): ')
                y = input('Columna (Y): ')
                while not y.isnumeric() or int(y) > (len(grid)-1):
                    print('Ingreso invรกlido')
                    y = input('Columna (Y): ')
                if e_grid[int(y)][int(x)] == '--':
                    e_grid[int(y)][int(x)] = grid[int(y)][int(x)] 
                    show_grid(e_grid)
                    print('Encuentra su par')
                    if jugador.pistas > 0:
                        pista = input('ยฟQuieres usar una pista?(s/n): ').lower()
                        while pista != 's' and pista != 'n':
                                print('Ingreso invรกlido')
                                pista = input('ยฟQuieres usar una pista?(s/n): ').lower()
                    else:
                        pista = 'n'
                    if pista == 'n':
                            i = input('Fila (X): ')
                            while not i.isnumeric() or int(i) > (len(grid)-1):
                                print('El valor que ingresaste no es vรกlido')
                                i = input('Fila (X): ')
                            j = input('Columna (Y): ')
                            while not j.isnumeric() or int(j) > (len(grid)-1):
                                print('El valor que ingresaste no es vรกlido')
                                j = input('Fila (X): ')
                            e_grid[int(j)][int(i)] = grid[int(j)][int(i)]
                            if e_grid[int(j)][int(i)] == e_grid[int(y)][int(x)]:
                                print('CORRECTO')
                                show_grid(e_grid)
                                print('\n')
                            else:
                                print('INCORRECTO')
                                jugador.quitar_vidas(1/4)
                                e_grid[int(j)][int(i)] = e_grid[int(y)][int(x)] = '--'
                                print('\n')
                                show_grid(e_grid)
                    else:
                        jugador.pistas = jugador.pistas -  1
                        for i in range(len(grid)):
                                for j in range(i+1):
                                        if grid[int(y)][int(x)] == grid[i][j]:
                                                e_grid[i][j] = grid[i][j]
                                        elif grid[int(y)][int(x)] == grid[j][i]:
                                                e_grid[j][i] = grid[j][i]
                        show_grid(e_grid)
                else:
                    print('Hey, cuidado porque ya habias volteado esta celda!')
                if e_grid == grid:
                    print (f'Felicitaciones {jugador.avatar}!')
                    print(f'Haz ganado una {recompensa}, lo puedes ver en tu inventario!')
                    jugador.agregar_inv(recompensa)
                    print('\n')
                    salida = input('Escribe (f) para regresar: ')
                    while not salida == 'f':
                        salida = input('Por favor, escribe (f) para regresar: ')
                    os.system('clear')
                    break