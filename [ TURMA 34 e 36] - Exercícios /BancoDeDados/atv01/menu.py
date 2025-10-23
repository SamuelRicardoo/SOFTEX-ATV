import query as q
from connection import criar_tabela

criar_tabela()
q.mocar_dados()

def exibir_menu():
    print('1. Mostrar todos os registros da tabela Aluno')
    print('2. Exibir nome e nota1 de todos os alunos')
    print('3. Listar alunos com nota2 maior que 8')
    print('4. Mostrar alunos nascidos após o ano de 2000')
    print('5. Exibir nome e mensalidade dos cursos com mensalidade > 600')
    print('6. Mostrar nome das turmas e ano, ordenados pelo ano (crescente)')
    print('7. Listar ano das turmas e quantidade por ano')
    print('8. Calcular média da nota1 por turma_id')
    print('9. Mostrar anos com mais de 2 turmas')
    print('10. Exibir nome dos cursos e mensalidades, ordenados por mensalidade (decrescente)')
    print('11. Sair')
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
            resultado = q.exibir_nome_e_nota1()
            print("\n--- Nome e Nota1 dos Alunos ---")
            for r in resultado:
                print(r)

        elif opcao == '3':
            resultado = q.alunos_com_nota2_maior_que_8()
            print("\n--- Alunos com Nota2 > 8 ---")
            for r in resultado:
                print(r)

        elif opcao == '4':
            resultado = q.alunos_nascidos_apos_2000()
            print("\n--- Alunos Nascidos Após 2000 ---")
            for r in resultado:
                print(r)

        elif opcao == '5':
            resultado = q.cursos_com_mensalidade_maior_600()
            print("\n--- Cursos com Mensalidade > 600 ---")
            for r in resultado:
                print(r)

        elif opcao == '6':
            resultado = q.turmas_ordenadas_por_ano()
            print("\n--- Turmas Ordenadas por Ano ---")
            for r in resultado:
                print(r)

        elif opcao == '7':
            resultado = q.quantidade_turmas_por_ano()
            print("\n--- Quantidade de Turmas por Ano ---")
            for r in resultado:
                print(f"Ano: {r[0]} - Quantidade: {r[1]}")

        elif opcao == '8':
            resultado = q.media_nota1_por_turma()
            print("\n--- Média da Nota1 por Turma ---")
            for r in resultado:
                print(f"Turma ID: {r[0]} - Média Nota1: {r[1]:.2f}")

        elif opcao == '9':
            resultado = q.anos_com_mais_de_duas_turmas()
            print("\n--- Anos com Mais de 2 Turmas ---")
            for r in resultado:
                print(f"Ano: {r[0]} - Quantidade: {r[1]}")

        elif opcao == '10':
            resultado = q.cursos_ordenados_por_mensalidade()
            print("\n--- Cursos Ordenados por Mensalidade (Decrescente) ---")
            for r in resultado:
                print(f"Curso: {r[0]} - Mensalidade: R${r[1]:.2f}")

        elif opcao == '11':
            print("Encerrando o programa...")
            
            break
        else:
            print("Opção inválida. Tente novamente.")
            
menu_principal()