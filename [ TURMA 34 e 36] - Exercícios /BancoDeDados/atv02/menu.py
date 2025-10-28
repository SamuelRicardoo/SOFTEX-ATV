import query as q
from connection import criar_tabela

criar_tabela()  

def exibir_menu():
    print('1. Total de alunos cadastrados (COUNT)')
    print('2. Menor mensalidade dos cursos (MIN)')
    print('3. Maior nota1 registrada (MAX)')
    print('4. Valor total das mensalidades (SUM)')
    print('5. Média geral da nota2 dos alunos (AVG)')
    print('6. Sair')
    print('-----------------------------------------')

def menu_principal():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            resultado = q.total_alunos()
            print(f"\nTotal de alunos cadastrados: {resultado}")

        elif opcao == '2':
            resultado = q.menor_mensalidade()
            print(f"\nMenor mensalidade dos cursos: R${resultado:.2f}")

        elif opcao == '3':
            resultado = q.maior_nota1()
            print(f"\nMaior nota1 registrada: {resultado}")

        elif opcao == '4':
            resultado = q.total_mensalidades()
            print(f"\nValor total das mensalidades: R${resultado:.2f}")

        elif opcao == '5':
            resultado = q.media_nota2()
            print(f"\nMédia geral da nota2")


menu_principal()