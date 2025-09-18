#Atv 5 e ATV 6
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo if saldo >= 0 else 0

    def depositar(self, valor):
        self.__saldo += valor
        print(f"[DEPÓSITO] {self.titular} depositou R${valor}. Saldo atual: R${self.__saldo}")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"[SAQUE] {self.titular} sacou R${valor}. Saldo atual: R${self.__saldo}")
            return True
        else:
            print(f"{self.titular} tentou sacar R${valor}, mas não tem saldo suficiente (Saldo: R${self.__saldo})")
            return False
        
    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("O saldo não pode ser negativo!")

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, nasci em {self.data_nascimento}.")

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade

print("\n=== Criando pessoa ===")
p1 = Pessoa("Samuel", "10/05/2001", "12345678901", "MG123456")

p1.apresentar()

print("CPF inicial:", p1.get_cpf())
print("Identidade inicial:", p1.get_identidade())

p1.set_cpf("98765432100")
p1.set_identidade("RJ654321")

print("CPF atualizado:", p1.get_cpf())
print("Identidade atualizada:", p1.get_identidade())

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