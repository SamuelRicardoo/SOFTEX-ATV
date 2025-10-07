from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def processar(self,valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Procesando o pagamento de cartão de credito no valor de {valor}")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Procesando o pagamento no boleto no valor de {valor}")

c = CartaoCredito()
b = Boleto()

c.processar(200)
b.processar(20)