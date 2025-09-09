#Atv 5 e ATV 6
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"[DEPÓSITO] {self.titular} depositou R${valor}. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"[SAQUE] {self.titular} sacou R${valor}. Saldo atual: R${self.saldo}")
            return True
        else:
            print(f"{self.titular} tentou sacar R${valor}, mas não tem saldo suficiente (Saldo: R${self.saldo})")
            return False


print("=== Criando contas ===")
c1 = ContaBancaria("Samuel", 1000)
c2 = ContaBancaria("Erica", 200)

print("\n=== Operações com a conta do Samuel ===")
c1.depositar(500) 
c1.sacar(300)       
c1.sacar(1500)      

print("\n=== Operações com a conta da Erica ===")
resultado = c2.sacar(150)  
print("Operação bem-sucedida?", resultado)

resultado = c2.sacar(100)  
print("Operação bem-sucedida?", resultado)