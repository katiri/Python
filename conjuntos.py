conjunto = {1, 2, 3, 4}
print(conjunto)
print(type(conjunto))

# não permite duplicidade
conjunto_2 = {1, 1, 2, 2}
print(conjunto_2)

# adicioando e removendo elementos
conjunto.add(5)
print(conjunto)
conjunto.discard(2)
print(conjunto)

# união
conjunto_3 = {1, 2, 3, 4, 5}
conjunto_4 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto_3.union(conjunto_4)
print(conjunto_uniao)

# intersecção
conjunto_interseccao = conjunto_3.intersection(conjunto_4)
print(conjunto_interseccao)

# diferença
conjunto_diferenca = conjunto_3.difference(conjunto_4)
print(conjunto_diferenca)
conjunto_diferenca = conjunto_4.difference(conjunto_3)
print(conjunto_diferenca)

# diferença simétrica
conjunto_diferenca_simetrica = conjunto_3.symmetric_difference(conjunto_4)
print(conjunto_diferenca_simetrica)

# se é uum subconjunto de outro
conjunto_5 = {1, 2}
conjunto_subset = conjunto_5.issubset(conjunto_3)
print(conjunto_subset)
conjunto_subset = conjunto_3.issubset(conjunto_5)
print(conjunto_subset)

# se é um super conjunto
conjunto_superset = conjunto_3.issuperset(conjunto_5)
print(conjunto_superset)
conjunto_superset = conjunto_5.issuperset(conjunto_3)
print(conjunto_superset)

# convertendo lista pra conjunto para retirar duplicidade
lista = ["cachorro", "cachorro", "gato", "gato", "papagaio"]
print(lista)
conjunto_6 = set(lista)
print(conjunto_6)

# voltando para lista
lista = list(conjunto_6)
print(lista)
