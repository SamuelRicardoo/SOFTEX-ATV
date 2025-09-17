from ContaBancaria import ContaBancaria
from Pessoa import Pessoa

# Pessoa
p1 = Pessoa("Samuel", "12/07/2001", "999999999", "RG1234")
print("Nome:", p1.nome)
print("CPF:", p1.get_cpf())
p1.set_cpf("888888888")
print("Novo CPF:", p1.get_cpf())

# Conta
conta = ContaBancaria("Samuel", 300)
print("Saldo inicial:", conta.get_saldo())
conta.set_saldo(500)
print("Saldo atualizado:", conta.get_saldo())

conta.set_saldo(-100)  # não deve permitir