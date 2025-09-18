# Classe base Usuario
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        print("Olá, Usuário! Bem-vindo ao sistema.")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}")

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

    def saudacao(self):
        print("Olá, Cliente! Bem-vindo ao sistema.")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Saldo: R${self.saldo}")

class Funcionario(Usuario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario

    def saudacao(self):
        print("Olá, Funcionário! Bem-vindo ao sistema.")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Salário: R${self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, email, salario, departamento):
        super().__init__(nome, email, salario)
        self.departamento = departamento

    def saudacao(self):
        print("Olá, Gerente! Bem-vindo ao sistema.")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Departamento: {self.departamento}")

class Autenticacao:
    def login(self, usuario, senha):
        if hasattr(usuario, "senha") and usuario.senha == senha:
            print(f"Autenticação bem-sucedida para {usuario.nome}.")
            return True
        else:
            print(f"Falha na autenticação para {usuario.nome}.")
            return False

    def status(self):
        print("Status de Autenticacao")

class Permissao:
    def verificar_permissao(self, usuario, acao):
        permissoes = {
            'Cliente': ['visualizar_produtos', 'fazer_pedido'],
            'Funcionario': ['visualizar_produtos', 'fazer_pedido', 'gerenciar_estoque'],
            'Gerente': ['visualizar_produtos', 'fazer_pedido', 'gerenciar_estoque', 'gerenciar_funcionarios']
        }

        tipo_usuario = type(usuario).__name__
        if acao in permissoes.get(tipo_usuario, []):
            print(f"{usuario.nome} tem permissão para {acao}.")
            return True
        else:
            print(f"{usuario.nome} não tem permissão para {acao}.")
            return False

    def status(self):
        print("Status de Permissao")

class Administrador(Permissao, Autenticacao):
    pass


# ====== uso ======

# Cliente
cliente1 = Cliente("Samuel", "samuel@email.com", 1000)
cliente1.saudacao()
cliente1.exibir_informacoes()

# Gerente
gerente1 = Gerente("Erica", "erica@email.com", 5000, "Financeiro")
gerente1.saudacao()
gerente1.exibir_informacoes()

# Administrador
admin = Administrador()
admin.login(cliente1, "123") 
admin.verificar_permissao(gerente1, "gerenciar_funcionarios")
admin.status()  

print("\nOrdem de MRO do Administrador:")
for cls in Administrador.__mro__:
    print(cls)
