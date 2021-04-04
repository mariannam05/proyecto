from Juego import Juego
from api import *
import os
import string 
from random import randrange, choice
from colored import fg, bg, attr
from Sopa_de_Letras import *

#archivo donde esta la funcion que se usa en el juego de sopa de letras

def agragar_palabra(palabra, grid):
    grid_size = 15
    palabra = choice([palabra, palabra[::-1]])
    direccion = choice([[1,0], [0,1],[1,1]]) 
    xsize = grid_size if direccion[0] == 0 else grid_size - len(palabra) #tamaño de fila con o sin la palabra
    ysize = grid_size if direccion[1] == 0 else grid_size - len(palabra) #tamaño de columna con o sin la palabra
    x = randrange(0,xsize) #posicion de la palabra en x
    y = randrange(0,ysize) #posicion de la palabra en y
    for i in range(0,len(palabra)):
        grid[y + direccion[1] * i][x + direccion[0] * i] = palabra[i] #poner la palabra en el grid
    return grid