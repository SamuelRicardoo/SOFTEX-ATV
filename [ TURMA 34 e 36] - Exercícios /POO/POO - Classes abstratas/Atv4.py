from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("Carro em movimento.")

    def parar(self):
        print("Carro parado.")


#Como Carro implementa apenas um dos dois métodos (mover()), 
#ela continua sendo abstrata — ou seja, ainda não completou o "contrato" definido por Transporte.
