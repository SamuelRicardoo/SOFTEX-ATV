class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self.livros = []

    def pegar_livro(self,livro):
        self.livros.append(livro)

class Livro:
    def __init__(self,nome,genero):
        self.nome = nome
        self.genero = genero   

pessoa1 = Pessoa("JAMAL")
livro1 = Livro("Vacabrejo", "ação")

pessoa1.pegar_livro(livro1)

for livro in pessoa1.livros:
    print(f"Livro: {livro.nome}, Gênero: {livro.genero}")