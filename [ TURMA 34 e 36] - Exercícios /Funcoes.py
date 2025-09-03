# --> 1
def saudacao():
    print("Olá, bem-vindo ao Python!")

# --> 2
def dobro(number):
    print(f"O doro é: {number * 2}")

# --> 3
def soma(param1,param2):
    print(f"A soma {param1 + param2}")

# --> 4
def mensagem(nome = "visitante"):
    print(f"Olá, {nome} !")

# --> 5
def operacao(param1,param2):
    print(f"A soma {param1 + param2}")
    print(f"A subtracao {param1 - param2}")
    print(f"A multiplicação {param1 * param2}")

# --> 6
def media(*args):
    print(f"A media é : {sum(args) / len(args)})

# --> 7
def dados_pessoais(**kwargs)
