# class Cuartos():
#     def __init__(self, obj_izq, obj_der, obj_cen, ubi):
#         self.obj_izq = obj_izq
#         self.obj_der = obj_der
#         self.obj_cen = obj_cen
#         self.ubi = ubi

#     def mostrar(self):
#         return (f'Objeto de la izquierda: {self.obj_izq} \nObjeto de la derecha: {self.obj_der} \nObjeto del centro: {self.obj_cen}')


# class Biblioteca(Cuartos):
#     def __init__(self,obj_izq, obj_der, obj_cen, ubi, game):
#         self.game = game
#         super().__init__(obj_izq,obj_der,obj_cen,"Biblioteca")

#     def mostrar(self):
#         return(f'Nombre del cuarto: {self.ubi} \nObjeto de la izquierda: {self.obj_izq} \nObjeto de la derecha: {self.obj_der} \nObjeto del centro: {self.obj_cen} \nCantidad de juegos: {self.game}')


# obj_izq= 'mueble para sentarse'
# obj_der = 'mueble de libros pequeño'
# obj_cen = 'mueble de biblioteca'
# game = 3
# ubi = 0

# nuevo_participante = Biblioteca(obj_izq, obj_der, obj_cen, ubi, game)
# print(nuevo_participante.mostrar())

from game import *


jugador = 'luis'
func_biblioteca(jugador)

