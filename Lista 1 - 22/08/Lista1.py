from random import randint

def atv1():
    count = 0
    point_rosariense_match=[0]*5
    point_adversario_match=[0]*5
    empate = 0
    vitoria = 0
    derrota = 0
    while(count < 5):
        print(f"Partidade {count+1}")
        point_rosariense_match[count] = int(input(f"Gols da Seleção Rosariense  no jogo {count+1}: "))
        point_adversario_match[count] = int(input(f"Gols da Seleção adversária no jogo {count+1}: "))
        count+=1
        
    for i in range(0,5):
        if(point_rosariense_match[i]< point_adversario_match[i]):
            derrota+=1
        elif (point_rosariense_match[i] > point_adversario_match[i]):
            vitoria+=1
        else:
            empate+=1        

    print("===Toneiro de Futebol===")
    print(f"Vitórias: {vitoria}")
    print(f"Empates: {empate}")
    print(f"Derrota: {derrota}")

def atv2():
    secret = randint(0,20)
    print("Voce tem 5 tentativas para adivinhar o número secreto")
    count = 0
    
    while (count <5):
        number= int(input(f"Tentativa N {count+1}: "))
        
        if number > secret:
            print("Muito Alto")
        elif number < secret:
            print("Muito Baixo!")
        else:
            print("Acertou!")
            break
        
        count+=1

def atv3():
    people = int(input("Quantas pessoas vão ao show: "))
    total = 0
    for i in range(0, people):
        age = int(input(f"Digite a idade da {i+1} Pessoa: "))
        
        if(age >= 18):
            print("Ingresso inteiro (R$ 20)")
            total+=20
        elif (age < 18 and age >=13):
            print("Meia entrada (R$ 10)")
            total+=10
        else:
            print("Entrada grátis")
    print(f"Total Arrecadado: R$ {total}")
            
def atv4():
    perguntas = [
        {
            "pergunta": "Qual a capital do Brasil?",
            "opcoes": ["1) São Paulo", "2) Brasília", "3) Rio de Janeiro"],
            "resposta": 2
        },
        {
            "pergunta": "Qual a Moeda do Brasil?",
            "opcoes": ["1) Real", "2) Euro", "3) Dolar"],
            "resposta": 1
        },
        {
            "pergunta": "Qual sigla representa PE",
            "opcoes": ["1) Paraiba", "2) Pernambuco", "3) Piaui"],
            "resposta": 2
        },
       {
            "pergunta": "Qual é a habilidade característica de Draven?",
            "opcoes": ["1) Axes spinning (Arremesso de Machado)", "2) Shadow Dash (Investida Sombria)", "3) Mystic Shot (Tiro Místico)"],
            "resposta": 1
        },
        {
            "pergunta": "Qual o efeito de matar um Dragão Elemental em League of Legends?",
            "opcoes": ["1) Concede buffs permanentes ao time", "2) Restaura mana imediatamente", "3) Gera ouro direto"],
            "resposta": 1
        }
    ]

    pontos = 0

    for i, q in enumerate(perguntas):
        print(f"\nPergunta {i+1}: {q['pergunta']}")
        for opcao in q['opcoes']:
            print(opcao)
         
        while True:
            try:
                resposta = int(input("Sua resposta (1, 2 ou 3): "))
                if resposta in [1, 2, 3]:
                    break
                else:
                    print("Escolha uma opção válida: 1, 2 ou 3")
            except ValueError:
                print("Digite um número válido: 1, 2 ou 3")
        
        if resposta == q['resposta']:
            pontos += 1
 
    print(f"Pontuação Final {pontos}/5")
    
    if pontos == 5:
        print("Gênio!")
    elif pontos >= 3:
        print("Mandou bem!")
    elif pontos >= 1:
        print("Precisa estudar mais")
    else:
        print("Zerou o quiz 😢")       

def atv5():
    candidate1=[0]*3
    candidate2=[0]*3
    candidate3=[0]*3
    
    for i in range(0,3):
        candidate1[i] = int(input(f"Nota do avaliador {i+1} para o candidato 1: "))
        candidate2[i] = int(input(f"Nota do avaliador {i+1} para o candidato 2: "))
        candidate3[i] = int(input(f"Nota do avaliador {i+1} para o candidato 3: "))
    
    total1 = sum(candidate1)
    total2 = sum(candidate2)
    total3 = sum(candidate3)
     
    print("\nPontuação final:")
    print(f"Candidato 1: {total1}")
    print(f"Candidato 2: {total2}")
    print(f"Candidato 3: {total3}")

    if total1 > total2 and total1 > total3:
        print("Candidato 1 é o campeão!")
    elif total2 > total1 and total2 > total3:
        print("Candidato 2 é o campeão!")
    elif total3 > total1 and total3 > total2:
        print("Candidato 3 é o campeão!")
    else:
        print("Empate! Disputa acirrada")
    
def atv6():
    
    name = str(input("Digite o nome do aluno: "))
    grade = float(input("Digite a nota do aluno: "))
    
    phrase =[]
    phrase.append(name)
    if(grade >= 7):
        phrase.append(" está Aprovado!")
    elif (grade <= 6.9 and grade > 5):
        phrase.append(" está Em Reposição!")
    else:
        phrase.append(" está Reprovado")
        
    print("".join(phrase))    

def menu():
    game = True
    while True:
        print("\n=== Menu de Atividades ===")
        print("1 - Campeonato de Futebol")
        print("2 - Adivinhação de Número")
        print("3 - Show e Arrecadação")
        print("4 - Quiz")
        print("5 - Competição de Candidatos")
        print("6 - Situação do Aluno")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            atv1()
        elif escolha == "2":
            atv2()
        elif escolha == "3":
            atv3()
        elif escolha == "4":
            atv4()
        elif escolha == "5":
            atv5()
        elif escolha == "6":
            atv6()
        elif escolha == "0":
            game = False
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Escolha um número entre 0 e 6.")
            
menu()