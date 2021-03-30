class Player():
    def __init__(self, username, contraseña, edad, avatar):
        self.username = username
        self.contraseña = contraseña
        self.edad = edad
        self.avatar = avatar

    def mostrar(self):
        print(f'Username: {self.username} \nEdad: {self.edad} \nAvatar: {self.avatar}')
    
    

