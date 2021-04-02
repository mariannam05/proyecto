class Juegos():
    def __init__(self,name, reglas, recompensa, position):
        self.name = name
        self.recompensa = recompensa
        self.reglas = reglas
        self.position = position

    def mostrar(self):
        print(f'''
        Nombre del juego: {self.name}
        Estas son las reglas del juego: {self.reglas}
        La recomensa de este juego es: {self.recompensa}
        Posicion del juego: {self.position}
        ''')
        