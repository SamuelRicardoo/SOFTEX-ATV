from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

c = Cachorro()
g = Gato()

c.falar()  
g.falar()  