# módulos -> arquivos .py que intereagem entre si

# em outro arquivo:
if __name__ == "__main__":
    # sempre que este arquivo for executado tudo que está aqui dentro vai ser executado também, porém, no caso desse
    # arquivo ser execuado através de outro arquivo, o que estiver aqui não é executado
    pass

# importando modulos e usando suas funcoes e classes

# importando o modulo metodos_funcoes_e_classes
import metodos_funcoes_e_classes
print(metodos_funcoes_e_classes.soma(10, 2))
print(metodos_funcoes_e_classes.subtracao(10, 2))

calculadora = metodos_funcoes_e_classes.Calculadora(10, 2)
print(calculadora.soma())

# importando apenas a classe Televisao do modulo metodos_funcoes_e_classes
from metodos_funcoes_e_classes import Televisao
televisao = Televisao()
print(televisao.estado)
televisao.power()
print(televisao.estado)
print(televisao.canal)
televisao.aumenta_canal()
televisao.aumenta_canal()
print(televisao.canal)
televisao.diminui_canal()
print(televisao.canal)

# importando mais de uma classe/funcao do modulo metodos_funcoes_e_classes
from metodos_funcoes_e_classes import Televisao, soma
televisao = Televisao()
print(televisao.estado)
televisao.power()
print(televisao.estado)
print(televisao.canal)
televisao.aumenta_canal()
televisao.aumenta_canal()
print(televisao.canal)
televisao.diminui_canal()
print(televisao.canal)

print(soma(30, 4))

# importando tudo do modulo metodos_funcoes_e_classes
from metodos_funcoes_e_classes import *
print(soma(10, 2))
print(subtracao(10, 2))

calculadora = Calculadora(10, 2)
print(calculadora.soma())

televisao = Televisao()
print(televisao.estado)
televisao.power()
print(televisao.estado)
print(televisao.canal)
televisao.aumenta_canal()
televisao.aumenta_canal()
print(televisao.canal)
televisao.diminui_canal()
print(televisao.canal)

# funcoes anonimas, lambda

# função contados_letras vai receber "lista" e vai retornar uma lista com os tamanhos de cada elemento dentro da lista
contador_letras = lambda lista: [len(x) for x in lista]
lista_str = ["cachorro", "gato", "passarinho"]
print(contador_letras(lista_str))

# soma
soma = lambda a, b: a + b
print(soma(10, 5))

# dicionário
dicionario = {
    "nome": "joão",
    "idade": 19,
    "sexo": "masculino"
}

print(dicionario)
print(dicionario["nome"])
print(dicionario["idade"])
print(dicionario["sexo"])

# transformando uma tupla de listas em um dicionário
tupla_lista = [("nome", "joão"), ("idade", 19), ("sexo", "masculino")]
print(tupla_lista)
transformado_dicionario = dict(tupla_lista)
print(transformado_dicionario)

# evitando erro de chave, se não achar o primeiro argumento mostra o outro
print(transformado_dicionario.get("nome", "Índice não encontrado"))
print(transformado_dicionario.get("teste", "Índice não encontrado"))

# verificando se existe uma certa chave em um dicionario (booleano)
print("nome" in transformado_dicionario)
print("teste" in transformado_dicionario)

# verificando se existe um valor em um dicionario (booleano)
print("joão" in transformado_dicionario.values())
print("arthur" in transformado_dicionario.values())

# adicionando valores em um dicionario
transformado_dicionario["Nova chave"] = "Novo valor"
print(transformado_dicionario)

# removendo itens de um dicionario
del transformado_dicionario["Nova chave"]
print(transformado_dicionario)

# verificando se uma chave existe durante a exclusão, caso exista, antes de excluir, pop mostra o valor da chave
print(transformado_dicionario.pop("Nova chave", "Chave não exite"))
print(transformado_dicionario.pop("sexo", "Chave não exite"))
print(transformado_dicionario)

# juntando dois dicionários
dicionario_1 = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'João': '8887-7778'}
print(dicionario_1)
dicionario_2 = {'Yan': '1234-5678', 'Fernando': '4345-5434', 'Luiza': '4567-7654'}
print(dicionario_2)

for nome in dicionario_2:
    dicionario_1[nome] = dicionario_2[nome]

print(dicionario_1)
# ou
dicionario_3 = {'Roger': '1234-5678', 'Fernanda': '4345-5434', 'Luiz': '4567-7654'}
print(dicionario_3)
dicionario_1.update(dicionario_3)
print(dicionario_1)

# atualizando os valores de um dicionario de forma fácil
dicionario_1_novo = {nome: '9' + dicionario_1[nome] for nome in dicionario_1}
print(dicionario_1_novo)

# acessando valores de um dicionario
print(dicionario_1_novo.values())

# calculadora com funções anônimas e dicionario
# função anonima não necessariamente precisa de nome
calculadora = {
    "soma": lambda a, b: a + b,
    "subtração": lambda a, b: a - b,
    "multiplicação": lambda a, b: a * b,
    "divisão": lambda a, b: a / b
}

print(calculadora["soma"](10, 2))
soma = calculadora["soma"]
print(soma(56, 90))
subtracao = calculadora["subtração"]
print(subtracao(56, 90))
multiplicacao = calculadora["multiplicação"]
print(multiplicacao(56, 90))
divisao = calculadora["divisão"]
print(divisao(56, 90))