## Dobro dos números (map + lambda)
lista = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, lista))
print(dobro)

## Filtrar números pares (filter + lambda)
lista_pares = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, lista_pares))
print(pares)


## Somar todos os números (reduce + lambda)
from functools import reduce
lista2 =  [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, lista2)
print(soma)

## Ordenar comprimento das strings (sorted + lambda)
strings = ["uva", "banana", "maçã", "laranja"]
ordenado = sorted(strings, key=lambda x: len(x))
print(ordenado)

#Pimeira letra maiúscula (map + lambda)
nomes = ["ana", "pedro", "maria"]
capitalizados = list(map(lambda x: x.capitalize(), nomes))
print(capitalizados)

## Produto dos numeros multiplos (reduce + lambda)
lista3 = [2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, lista3)
print(produto)

#Ordenar por último caractere (sorted + lambda)
palavras = ["banana", "uva", "maçã", "laranja"]
ordenado_ultimo = sorted(palavras, key=lambda x: x[-1])
print(ordenado_ultimo)
