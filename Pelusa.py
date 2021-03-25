from Player import *
class Pelusa(Player):
    def __init__(self, username, contraseña, edad, avatar, time=0,vida=0):
        Player.__init__(self,username,contraseña,edad,'Pelusa')
    
    def mostrar(self):
        return (f'Username: {self.username} \nEdad: {self.edad} \nAvatar: {self.avatar} \nTime: {self.time}')
    
    def mostrar_vt(self):
        return (f'Su vida es de {self.vida} y su tiempo para terminar el juego es de: {self.time} minutos')