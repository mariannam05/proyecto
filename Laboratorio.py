from Cuarto import Cuarto

class Laboratorio(Cuarto):
    def __init__(self,obj_izq, obj_der, obj_cen, ubi, game):
        self.game = game
        super().__init__(obj_izq,obj_der,obj_cen,"Laboratorio SL-001")

    def mostrar(self):
        return(f'Nombre del cuarto: {self.ubi} \nObjeto de la izquierda: {self.obj_izq} \nObjeto de la derecha: {self.obj_der} \nObjeto del centro: {self.obj_cen} \nCantidad de juegos: {self.game}')

     