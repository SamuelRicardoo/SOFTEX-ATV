#AtV 7 e ATV 8
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []  

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"{aluno.nome} adicionado à turma.")

    def mostrar_alunos(self):
        print("=== Lista de Alunos ===")
        for aluno in self.alunos:
            print(aluno)


a1 = Aluno("Samuel", 9.5)
a2 = Aluno("Nathalia", 8.0)
a3 = Aluno("Julio", 10.0)

turma1 = Turma()

turma1.adicionar_aluno(a1)
turma1.adicionar_aluno(a2)
turma1.adicionar_aluno(a3)

turma1.mostrar_alunos()