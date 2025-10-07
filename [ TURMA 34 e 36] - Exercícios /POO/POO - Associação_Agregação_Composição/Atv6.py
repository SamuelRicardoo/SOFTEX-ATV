class Sala:
    def __init__(self):
        print("Sala criada!")

    def __del__(self):
        print("Sala destruído!")

class Cozinha:
    def __init__(self):
        print("Cozinha criada!")

    def __del__(self):
        print("Cozinha destruído!")

class Quarto:
    def __init__(self):
        print("Quarto criada!")

    def __del__(self):
        print("Quarto destruído!")


class Casa:
    def __init__(self):
        print("Casa Criada!")
        self.sala = Sala()  
        self.cozinha = Cozinha()
        self.quarto = Quarto()

    def __del__(self):
        print("Casa Destruida")

casa = Casa()
del casa