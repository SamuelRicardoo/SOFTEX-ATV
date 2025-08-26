#1
contato = {
    "nome": "Lucas",
    "idade": 25,
     "email": "lucas@gmail.com"}
    
#2
cliente = {"nome": "Amanda", "idade": 31}

telefone = cliente.get('telefone')
if telefone is not None:
    print(telefone)
else:
    print("Não informado")



#3
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
for x, obj in livro.items():
    print(f"{x}: {obj}")


#4
livro["disponivel"] = True
print(livro)

#5
livro.pop("ano")
print(livro)

#6
compras = {
    "arroz": 12.50,
    "feijão": 8.30,
    "macarrão": 5.70
}

total =sum(compras.values())
print(total)

#7
frutas = {"maçã": 3, "banana": 5, "laranja": 2}

for fruta, quantidade in frutas.items():
    if quantidade > 2:
        print(fruta)

#8
usuario = {"login": "joaosilva"}
senha = cliente.get('senha')

if senha is not None:
    print("SENHA PRESENTE")
else:
    usuario["senha"] = "123456"

print(usuario)


#9
capitais = {
    "SP": "São Paulo", 
    "RJ": "Rio de Janeiro",
    "MG": "Belo Horizonte"}
    
for chave, estado in capitais.items():
    if chave == "SP":
        print(f"A Capital de {chave} é {estado}")


#10
produto = {"nome": "Teclado", "estoque": 15}
produto.update({"estoque": produto.get("estoque") + 10})
print(produto)
