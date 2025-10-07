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

animal = Animal()

#Um metodo abstrado não pode ser instanciado. 
#Para ser utilizado é preciso utilizar subclasse para implemetar o uso dela.