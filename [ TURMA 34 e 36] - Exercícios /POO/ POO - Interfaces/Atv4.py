from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {}

    def salvar(self, objeto):
        id = len(self.dados) + 1
        self.dados[id] = objeto

    def buscar(self, id):
        return self.dados.get(id, None)

repo = RepositorioMemoria()
repo.salvar("Engenheiro de Software")
obj = repo.buscar(1)
print("Objeto:", obj)
