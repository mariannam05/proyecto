from Player import *
class Usuario(Player):
    def __init__(self, username, contraseña, edad, avatar, pistas, vidas, tiempo, win, inventario, dificultad):
        self.pistas = pistas
        self.vidas = vidas
        self.tiempo = tiempo
        self.win = win
        self.inventario = inventario
        self.dificultad = dificultad
        Player.__init__(self, username, contraseña, edad, avatar)
        

    def agregar_inv(self, object):
        self.inventario.append(object)

    def selec_win(self):
        self.win = True
    
    def agregar_vida(self, cantidad):
        if cantidad == 0:
            print('Ya obtuviste esta vida')
        else:
            print(f'+{cantidad} vidas')
            self.vidas = self.vidas + cantidad
    
    def quitar_vidas(self, cantidad):
        print(f'-{cantidad} vidas')
        self.vidas = self.vidas - cantidad

    def mostrar_atri(self):
        print(f'''
        Vidas: {self.vidas}
        Pistas: {self.pistas}
        Inventario: {self.inventario}
        ''')