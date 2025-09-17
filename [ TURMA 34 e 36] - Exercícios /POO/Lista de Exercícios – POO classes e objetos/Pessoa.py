class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf

    def get_identidade(self):
        return self.__identidade

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade