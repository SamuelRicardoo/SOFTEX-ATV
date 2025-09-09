#ATV 9
class Cachorro:
    def __init__(self, nome, idade):
        self.especie = "Canis Familiaris"
        self.nome = nome
        self.idade = idade
        
c1 = Cachorro("Rex", 5)
print(f"{c1.nome} é da especie {c1.especie}")