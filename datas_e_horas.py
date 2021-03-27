# importando funções e classes de datas e horas
from datetime import *

# data
data_atual = date.today()
print(data_atual)
print(type(data_atual))

# formatando data
print(data_atual.strftime("%d/%m/%y"))
print(data_atual.strftime("%d-%m-%y"))
print(data_atual.strftime("%d %m %y"))

print(type(data_atual.strftime("%d/%m/%y")))

# dia da semana, nome do mês e ano inteiro
print(data_atual.strftime("%A %B %Y"))
print(data_atual.strftime("%a %b %Y"))

# hora
hora_atual = time(hour=15, minute=18, second=30)
print(hora_atual)
print(type(hora_atual))

# formatando hora
print(hora_atual.strftime("%H-%M-%S"))
print(type(hora_atual.strftime("%H-%M-%S")))

# data e hora
tempo_atual = datetime.now()
print(tempo_atual)
print(type(tempo_atual))

# formatando data e hora
print(tempo_atual.strftime("%d/%m/%Y %H:%M:%S"))
print(type(tempo_atual.strftime("%d/%m/%Y %H:%M:%S")))
print(tempo_atual.strftime("%c"))

# valores especificos
print(tempo_atual.day)
print(tempo_atual.month)
print(tempo_atual.year)
print(tempo_atual.hour)
print(tempo_atual.minute)
print(tempo_atual.second)
print(tempo_atual.microsecond)

print(type(tempo_atual.day))

# dia da semana
print(tempo_atual.weekday())
print(type(tempo_atual.weekday()))

# traduzindo
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(dias_da_semana[tempo_atual.weekday()])

# criar uma data
data_criada = datetime(2021, 6, 20, 15, 18, 30)
print(data_criada)
print(data_criada.strftime("%c"))

# convertendo string pra data
str_data = "01/02/2021"
data_convertida = datetime.strptime(str_data, "%d/%m/%Y")
print(data_convertida)
print(type(data_convertida))
print(dias_da_semana[data_convertida.weekday()])

str_data = "01/02/2021 22:23:00"
data_convertida = datetime.strptime(str_data, "%d/%m/%Y %H:%M:%S")
print(data_convertida)

# soma e subtração de datas
nova_data = data_convertida - timedelta(days=365, hours=2, minutes=3, seconds=10)
print(nova_data)
nova_data = data_convertida + timedelta(days=365, hours=2, minutes=3, seconds=10)
print(nova_data)

print(type(timedelta(hours=15)))