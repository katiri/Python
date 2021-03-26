# listas: mutável
lista_int = [1, 3, 4, 7]
lista_str = ["palavra1", "palavra2", "palavra3"]

print(lista_int)
print(type(lista_int))

lista_mista = [1, "palavra"]

# acessando valores através de posições
print(lista_str[0])

# percorrendo lista com laõ de repetição
for x in lista_int:
    print(x)

# somatoria
soma = 0
for x in lista_int:
    soma = soma + x

print(soma)

# ou, operação soma
print(sum(lista_int))

# outras funções
max(lista_int)
min(lista_int)
# em listas de strings busca em ordem alfabética

# verificando valor em uma lista
if 5 in lista_int:
    print("Existe o número 5 na lista")

# multiplicação com listas
nova_lista_int = lista_int * 3
print(nova_lista_int)

nova_lista_str = lista_str * 3
print(nova_lista_str)

# incluindo valores na lista posteriormente
lista_str.append("palavra4")
print(lista_str)
lista_str.insert(3, "palavra5")
print(lista_str)

# retirando itens da lista
lista_str.pop()
print(lista_str)
# ultimo valor
lista_str.pop(1)
print(lista_str)
# item da posição 1
lista_str.remove("palavra3")
print(lista_str)

# ordenando lista
lista_desordenada = [4, 33, 1, 5, 40]
print(lista_desordenada)
lista_desordenada.sort()
print(lista_desordenada)

# revertendo a ordem
lista_desordenada.reverse()
print(lista_desordenada)

# tuplas: imutáveis
tupla = (1, 10, 15, 14)
print(tupla)
print(tupla[3])
# tupla[3] = 12
# print(tupla)

# tamanho de lista e tupla (número de elementos)
print(len(lista_int))
print(len(tupla))

# converter lista em tupla e vice versa
tupla_desordenada = tuple(lista_desordenada)
print(tupla_desordenada)

lista_desordenada = list(tupla_desordenada)
print(lista_desordenada)
