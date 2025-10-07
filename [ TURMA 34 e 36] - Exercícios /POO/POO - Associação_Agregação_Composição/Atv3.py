class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
    def __str__(self):
        return f"{self.nome} - {self.cargo}"

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = [] 

    def adicionar_funcionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Departamento {self.nome} tem os seguintes funcionários:")
        for func in self.funcionarios:
            print(f"- {func}")

func1 = Funcionario("Samuel", "Engenheiro de Software")
func2 = Funcionario("Nathalia", "Analista")

dep = Departamento("Tecnologia")
dep.adicionar_funcionario(func1)
dep.adicionar_funcionario(func2)

dep.listar_funcionarios()