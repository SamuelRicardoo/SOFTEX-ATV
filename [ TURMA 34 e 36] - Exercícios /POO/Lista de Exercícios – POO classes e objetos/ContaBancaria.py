class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.__saldo = saldo 

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo!") 