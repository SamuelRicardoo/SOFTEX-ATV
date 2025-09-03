# --> 1
def atv1():
    def saudacao():
        print("Olá, bem-vindo ao Python!")
    
    saudacao()

# --> 2
def atv2():
    def dobro(number):
        print(f"O dobro é: {number * 2}")
   
    dobro(5)

# --> 3
def atv3():
    def soma(param1, param2):
        print(f"A soma é {param1 + param2}")
   
    soma(3, 7)

# --> 4
def atv4():
    def mensagem(nome="visitante"):
        print(f"Olá, {nome}!")
    
    mensagem()
    mensagem("Samuel")

# --> 5
def atv5():
    def operacao(param1, param2):
        print(f"A soma é {param1 + param2}")
        print(f"A subtração é {param1 - param2}")
        print(f"A multiplicação é {param1 * param2}")
    
    operacao(10, 5)

# --> 6
def atv6():
    def media(*args):
        print(f"A média é: {sum(args) / len(args)}")
    
    media(7, 8, 9, 10)

def atv7():
    def dados_pessoais(**kwargs):
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")

    dados_pessoais(nome="Samuel", idade=24, cidade="Recife")

# --> 8
def atv8():
    def calculadora():
        def somar(x, y): return x + y
        def subtrair(x, y): return x - y
        def multiplicar(x, y): return x * y
        def dividir(x, y): return x / y if y != 0 else "Erro: divisão por zero!"

        print("Escolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        escolha = 1   
        a, b = 10, 5 

        print(f"\nExemplo: escolha={escolha}, a={a}, b={b}")

        if escolha == 1:
            print("Resultado:", somar(a, b))
        elif escolha == 2:
            print("Resultado:", subtrair(a, b))
        elif escolha == 3:
            print("Resultado:", multiplicar(a, b))
        elif escolha == 4:
            print("Resultado:", dividir(a, b))
        else:
            print("Opção inválida!")

    calculadora()

# --> 9
def atv9():
    def aplicar_operacao(a, b, operacao):
        return operacao(a, b)

    def soma(x, y): return x + y
    def subtracao(x, y): return x - y
    def multiplicacao(x, y): return x * y
    def divisao(x, y): return x / y if y != 0 else "Erro: divisão por zero!"

    print("Soma:", aplicar_operacao(10, 5, soma))
    print("Subtração:", aplicar_operacao(10, 5, subtracao))
    print("Multiplicação:", aplicar_operacao(10, 5, multiplicacao))
    print("Divisão:", aplicar_operacao(10, 5, divisao))
    print("Divisão por zero:", aplicar_operacao(10, 0, divisao))

atividades = [atv1, atv2, atv3, atv4, atv5, atv6, atv7, atv8, atv9]

for i, func in enumerate(atividades, start=1):
    print(f"\n---Atividade-{i}---")
    func()