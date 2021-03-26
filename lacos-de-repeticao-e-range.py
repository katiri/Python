# percorrendo os números de 0 a 100
for x in range(100):
    print(x)

# começa do 1
for x in range(1, 100):
    print(x)

# descobrindo se um número é primo
a = int(input("Digite um valor: "))

teste = "O valor é primo"
for x in range(2, a):
    resto = a % x
    if resto == 0:
        teste = "O valor não é primo"

print(teste)

# verificando quais números de 1 a 100 são primos
for x in range(1, 101):
    teste = str(x) + " é primo"
    for y in range(2, x):
        resto = x % y
        if resto == 0:
            teste = str(x) + " não é primo"
    print(teste)

# while
i = 0
while i < 10:
    print(i)
    i += 1
