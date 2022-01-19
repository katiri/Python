from __future__ import annotations


class Data():
    dia = None
    mes = None
    ano = None

    def __init__(self, diaI, mesI, anoI):
        self.dia = diaI
        self.mes = mesI
        self.ano = anoI

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

data = Data(10, 10, 2010)
# data.dia = 10
# data.mes = 10
# data.ano = 2010

print(data)