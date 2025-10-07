from abc import ABC, abstractmethod

class Imprimivel(ABC):

    @abstractmethod
    def imprimir(self):
        pass

class Exportavel (ABC):

    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel,Exportavel):
    def imprimir(self):
        print("Imprimindo relatório em papel...")

    def exportar(self):
        print("Exportando relatório em PDF...")

relatorio = Relatorio()

relatorio.imprimir()
relatorio.exportar()