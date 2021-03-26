# método/função
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print(soma(1, 2))
print(soma(4, 5))

print(subtracao(2, 1))
print(subtracao(4, 1))

print(multiplicacao(2, 1))
print(multiplicacao(4, 1))

print(divisao(2, 1))
print(divisao(4, 1))

# classes
class Calculadora:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

calculadora = Calculadora(10, 2)
print(calculadora.a, calculadora.b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())

# class Calculadora:
#     def soma(self, a, b):
#         return a + b
#
#     def subtracao(self, a, b):
#         return a - b
#
#     def multiplicacao(self, a, b):
#         return a * b
#
#     def divisao(self, a, b):
#         return a / b
#
# calculadora = Calculadora()
# print(calculadora.soma(10, 2))
# print(calculadora.subtracao(10, 2))
# print(calculadora.multiplicacao(10, 2))
# print(calculadora.divisao(10, 2))

class Televisao:
    def __init__(self):
        self.estado = False
        self.canal = 0

    def power(self):
        if self.estado:
            self.estado = False
        else:
            self.estado = True

    def aumenta_canal(self):
        if self.estado:
            self.canal += 1

    def diminui_canal(self):
        if self.estado:
            self.canal -= 1

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