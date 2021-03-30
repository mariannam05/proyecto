class Player():
    def __init__(self, username, contraseña, edad, avatar, time=0,vida=0, pistas=0):
        self.username = username
        self.contraseña = contraseña
        self.edad = edad
        self.avatar = avatar
        self.time = time
        self.vida = vida
        self.pistas = pistas

    def mostrar(self):
        print(f'Username: {self.username} \nEdad: {self.edad} \nAvatar: {self.avatar}')
    
    

