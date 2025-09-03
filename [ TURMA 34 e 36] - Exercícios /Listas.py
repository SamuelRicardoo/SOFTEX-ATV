def atv1():
    livros = ["JAMAL", "O Pequeno Tigre", "O COMPASSO"]
    print(livros)

def atv2():
    livros = ["JAMAL", "O Pequeno Tigre", "O COMPASSO"]
    print("Primeiro livro:", livros[0])
    print("Último livro:", livros[-1])

def atv3():
    livros = ["JAMAL", "O Pequeno Tigre", "O COMPASSO"]
    
    livros.append("Maik Dos Livros")
    livros.append("TUDO DE NOVO")
    print(livros)
    
def atv4():
    livros = ["JAMAL", "O Pequeno Tigre", "O COMPASSO"]
    livros.insert(1, "Duna")
    print(livros)

def atv5():
    livros = ["JAMAL", "O Pequeno Tigre", "O COMPASSO"]
    
    try:
        livros.remove("Silêncio dos inocentes")
    except ValueError:
        print("Livro não encontrado")
        
    print(livros)

def atv6():
    numeros = [1, 2, 3, 2, 4, 2, 5]
    quantidade = numeros.count(2)
    print("O número 2 aparece", quantidade, "vezes na lista.")
    
def atv7():
    livros = ["JAMAL", "O Pequeno Tigre", "O COMPASSO"]

    for livro in livros:
        print(f"O livro {livro} é interessante")

def atv8():
    idades = [12, 18, 25, 14, 30]

    for idade in idades:
        if idade >= 18:
            print(idade)

def atv9():
    valores = [10, 20, 30, 40]
    soma = 0
    
    for valor in valores:
        soma += valor

    print("A soma dos valores é:", soma)
    
def atv10():
    notas = []

    for i in range(2):
        aluno = []
        print(f"Digite as 3 notas do aluno {i+1}:")
        for j in range(3):
            nota = float(input(f"Nota {j+1}: "))
            aluno.append(nota)
        notas.append(aluno)

    for i, aluno in enumerate(notas):
        media = sum(aluno) / len(aluno)
        print(f"Média do aluno {i+1}: {media:.2f}")

def atv11():
    
    tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

    tabuleiro[1] = ["pea"]*8
    tabuleiro[6] = ["pea"]*8

    pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
    tabuleiro[0] = pecas.copy()
    tabuleiro[7] = pecas.copy()

    for linha in tabuleiro:
        print(" ".join(linha))

def menu():
    
    switch ={
        "1": atv1, "2": atv2, "3": atv3,"4": atv4,
        "5": atv5,"6": atv6,"7": atv7,"8": atv8,
        "9": atv9,"10": atv10,"11": atv11 
    }
    
    print("===== MENU DE ATIVIDADES =====")
    print("1  - Criar lista de livros e exibir")
    print("2  - Exibir primeiro e último livro")
    print("3  - Adicionar livros com append()")
    print("4  - Inserir livro 'Duna' na segunda posição")
    print("5  - Remover livro 'Silêncio dos inocentes'")
    print("6  - Contar quantas vezes o número 2 aparece")
    print("7  - Exibir cada livro como interessante")
    print("8  - Exibir idades maiores ou iguais a 18")
    print("9  - Calcular soma manual dos valores")
    print("10 - Receber notas de alunos e calcular média")
    print("11 - Criar e exibir tabuleiro de xadrez")
    print("===============================")

    escolha = input("Digite o número da opção desejada: ")
    acao = switch.get(escolha)
    if acao:
        acao()
    else:
        print("Opção Invalida")

menu()