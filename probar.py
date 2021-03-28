class Cuartos():
    def __init__(self, obj_izq, obj_der, obj_cen, ubi):
        self.obj_izq = obj_izq
        self.obj_der = obj_der
        self.obj_cen = obj_cen
        self.ubi = ubi

    def mostrar(self):
        return (f'Objeto de la izquierda: {self.obj_izq} \nObjeto de la derecha: {self.obj_der} \nObjeto del centro: {self.obj_cen}')


class Biblioteca(Cuartos):
    def __init__(self,obj_izq, obj_der, obj_cen, ubi, game):
        self.game = game
        super().__init__(obj_izq,obj_der,obj_cen,"Biblioteca")

    def mostrar(self):
        return(f'Nombre del cuarto: {self.ubi} \nObjeto de la izquierda: {self.obj_izq} \nObjeto de la derecha: {self.obj_der} \nObjeto del centro: {self.obj_cen} \nCantidad de juegos: {self.game}')


obj_izq= 'mueble para sentarse'
obj_der = 'mueble de libros pequeño'
obj_cen = 'mueble de biblioteca'
game = 3
ubi = 0

nuevo_participante = Biblioteca(obj_izq, obj_der, obj_cen, ubi, game)
print(nuevo_participante.mostrar())

# class Participante:
#     def __init__(self,nombre,solo,categoria,telefono,num_registro):
#         self.nombre = nombre
#         self.solo = solo
#         self.categoria = categoria
#         self.telefono = telefono
#         self.num_registro = num_registro

#     def mostrar(self):
#         return(f"Nombre: {self.nombre}\nSolo/Grupo: {self.solo}\nCategoría: {self.categoria}\nTeléfono: {self.telefono}\nNúmero de registro: {self.num_registro}")


# class Musica(Participante):
#     def __init__(self,nombre,solo,categoria,telefono,num_registro,instrumento):
#         self.instrumento = instrumento
#         super().__init__(nombre,solo,"Música",telefono,num_registro)

#     def mostrar(self):
#         return(f"Nombre: {self.nombre}\nSolo/Grupo: {self.solo}\nCategoría: {self.categoria}\nTeléfono: {self.telefono}\nNúmero de registro: {self.num_registro}\nInstrumento(s): {self.instrumento}")

# nombre = 'luis'
# solo = 's'
# telefono = '0212'
# num_registro = '1234'
# instrumento = 'guitarra'
# print("\n1. Canto\n2. Baile\n3. Música\n4. Libre\n")
# categoria = input("Introduzca el número correspondiente a su categoría: ")
# if int(categoria) == 3:
#         instrumento = 'guitarra'
#         nuevo_participante = Musica(nombre,solo,categoria,telefono,num_registro,instrumento)
#         print(nuevo_participante.mostrar())
