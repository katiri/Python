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

# dicionario
dicionario = {
    "nome": "joão",
    "idade": 19,
    "sexo": "masculino"
}

print(dicionario)
print(dicionario["nome"])
print(dicionario["idade"])
print(dicionario["sexo"])

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