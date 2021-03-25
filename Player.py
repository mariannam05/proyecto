class Player():
    def __init__(self, username, contraseña, edad, avatar, time=0,vida=0):
        self.username = username
        self.contraseña = contraseña
        self.edad = edad
        self.avatar = avatar
        self.time = time
        self.vida = vida

    def mostrar(self):
        print(f'Username: {self.username} \nEdad: {self.edad} \nAvatar: {self.avatar}')
    
    # def mostrar_vt(self):
    #     return (f'Su vida es de {self.vida} y su tiempo para terminar el juego es de: {self.time} minutos')

