from abc import ABC, abstractmethod

class Ligavel(ABC):

    @abstractmethod
    def ligar(self):
        pass

class Desligavel (ABC):

    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel,Desligavel):
    def desligar(self):
        print("Desligando o Computador")
    
    def ligar(self):
        print("Ligando o Computador")

c = Computador()

c.ligar()
c.desligar()