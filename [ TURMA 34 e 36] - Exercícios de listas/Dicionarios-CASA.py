# 1
dis = {
    "nome": "Samuel",
    "idade": 18,
    "nota": 8.5
}
print(dis)

# 2
produto = {
    "nome": "Caneta",
    "preço": 2.5, 
    "estoque": 100
}
print(f"Nome: {produto['nome']} Estoque: {produto['estoque']}")


#3
pessoa = {
        "nome": "Carlos",
         "idade": 30
        }

pessoa["cidade"] = "São Paulo"
print(pessoa)

#4
carro = {
    "marca": "Ford",
    "modelo": "Fiesta", 
    "ano": 2010
}
carro.pop("ano")
print(carro)

#5
contato = {
    "nome": "Ana",
     "email": "ana@email.com"}

if 'telefone' in contato:
    print("A chave 'telefone' existe no dicionário!")
else:
    print("A chave 'telefone' não existe no dicionário.")

#6
def contar_frutas(palavras):
    somas = {
        "somaMaça": 0,
        "SomaBanana": 0,
        "SomaLaranja": 0,
    }

    for fruta in palavras:
        if fruta == 'maçã':
            somas["somaMaça"] += 1
        elif fruta == 'banana':
            somas["SomaBanana"] += 1
        elif fruta == 'laranja':
            somas["SomaLaranja"] += 1

    return somas

palavras = ["maçã", "banana","maçã","laranja","banana","maçã"]
resultado = contar_frutas(palavras)

print(f"Total: {resultado}")   



#7
d = {"a": 1, "b": 2, "c": 3}
invertido = {}

for chave, valor in d.items(): 
    invertido[valor] = chave  
print(invertido)


#8
alunos = [
    {"nome": "Samuel", "notas": [6, 6, 6]},
    {"nome": "Jamal", "notas": [5, 5, 5]},
     {"nome": "MAIKE", "notas": [3.5, 10, 10]}
]

for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    media = sum(notas) / len(notas)
    print(f"Aluno: {nome}, Média: {media:.2f}")


#9
def double_disc(disc1, disc2):

    resultCopy = disc1.copy()
    resultCopy.update(disc2)
    return resultCopy

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

result = double_disc(d1, d2)
print(result)

#10
def bubble_sort(array):

    items = list(array.items())
    
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    sorted_dict = dict(items)
    return sorted_dict

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

sorted_pontuacoes = bubble_sort(pontuacoes)
print(sorted_pontuacoes)
