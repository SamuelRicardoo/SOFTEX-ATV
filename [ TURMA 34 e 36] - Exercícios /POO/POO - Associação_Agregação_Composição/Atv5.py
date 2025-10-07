class Motor:
    def __init__(self):
        print("Motor criado!")

    def __del__(self):
        print("Motor destruído!")

class Carro:
    def __init__(self):
        print("Carro criado!")
        self.motor = Motor()  

    def __del__(self):
        print("Carro destruído!")

carro = Carro()
del carro