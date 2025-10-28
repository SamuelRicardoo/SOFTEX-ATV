import query as q
from connection import criar_tabela

criar_tabela()

def exibir_menu():
    print('1. Mostrar todos os alunos')
    print('2. Top 10 alunos por média (nota1 e nota2)')
    print('3. Mostrar alunos com dados da turma (Left Join)')
    print('4. Mostrar apenas alunos da turma 2')
    print('5. Sair')
    print('-----------------------------------------')

def menu_principal():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            resultado = q.mostrar_todos_alunos()
            print("\n--- Todos os Alunos ---")
            for r in resultado:
                print(r)

        elif opcao == '2':
            resultado = q.top10_por_media()
            print("\n--- Top 10 Alunos por Média ---")
            for r in resultado:
                print(f"Nome: {r[0]}, Nota1: {r[1]}, Nota2: {r[2]}, Média: {r[3]:.2f}")

        elif opcao == '3':
            resultado = q.alunos_com_turma()
            print("\n--- Alunos com Dados da Turma ---")
            for r in resultado:
                print(r)

        elif opcao == '4':
            resultado = q.alunos_turma2()
            print("\n--- Alunos da Turma 2 ---")
            for r in resultado:
                print(r)

        elif opcao == '5':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu_principal()