a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

# if e else
if a > b:
    print("O maior valor é", a)
else:
    print("O maior valor é", b)

# elif e and
c = int(input("Terceiro valor: "))
if a > b and a > c:
    print("O maior valor é", a)
elif b > a and b > c:
    print("O maior valor é", b)
else:
    print("O maior valor é", c)

# comparação e or
d = int(input("Quarto valor: "))
e = int(input("Quinto valor: "))
resto_d = d % 2
resto_e = e % 2

if resto_d == 0 or resto_e == 0:
    print("Pelo menos um dos dois valores é par")
else:
    print("Nenhum dos valores é par")

if resto_d != 0 or resto_e != 0:
    print("Pelo menos um dos dois valores é ímpar")
else:
    print("Nenhum dos valores é ímpar")

# "se isso for falso"
f = int(input("Sexto valor: "))

if not f > 10:
    print("O valor não é maior que 10")

# calculando média de notas
nota_1 = int(input("Nota do primeiro bimestre: "))
nota_2 = int(input("Nota do segundo bimestre: "))
nota_3 = int(input("Nota do terceiro bimestre: "))
nota_4 = int(input("Nota do quarto bimestre: "))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4
print(media)

if nota_1 <= 10 or nota_2 <= 10 or nota_3 <= 10 or nota_4 <= 10:
    if media >= 7:
        print("Aprovado")
    else:
        print("Rejeitado")
else:
    print("Uma das notas foi digitada errada, tente novamente")


print("Final do programa")