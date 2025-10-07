class Onibus:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def listar_alunos(self):
        return [aluno.nome for aluno in self.alunos]

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.onibus = None

    def subir_no_onibus(self, onibus):
        self.onibus = onibus
        onibus.adicionar_aluno(self)

    def mostrar_alunos_no_onibus(self):
        if self.onibus:
            alunos_no_onibus = self.onibus.listar_alunos()
            print(f"Alunos no ônibus {self.onibus.nome}: {', '.join(alunos_no_onibus)}")
        else:
            print(f"{self.nome} não está em nenhum ônibus.")

onibus1 = Onibus("LINHA VERDE")
aluno1 = Aluno("JAMAL")
aluno2 = Aluno("NATHALIA")

aluno1.subir_no_onibus(onibus1)
aluno2.subir_no_onibus(onibus1)

aluno1.mostrar_alunos_no_onibus()
aluno2.mostrar_alunos_no_onibus()
