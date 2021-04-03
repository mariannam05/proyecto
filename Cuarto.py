class Cuarto():
    def __init__(self, obj_izq, obj_der, obj_cen, ubi):
        self.obj_izq = obj_izq
        self.obj_der = obj_der
        self.obj_cen = obj_cen
        self.ubi = ubi

    def mostrar(self):
        return (f'Objeto de la izquierda: {self.obj_izq} \nObjeto de la derecha: {self.obj_der} \nObjeto del centro: {self.obj_cen}')

