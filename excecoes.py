# forçando um erro
# divisao = 10/0

# tratamento de execeçao (tratamento de erros)
# Existe uma árvore de exceções (documentação python)
# lista = [1, 10]
# try:
#     divisao = 10/0
#     lista[3]
#     x = a
# except ZeroDivisionError:
#     print("Não é possível fazer uma divisão por zero")
# except IndexError:
#     print("Erro ao tentar acessar um índice inválido da lista")
# except BaseException as ex:
#     print("Erro desconhecido:", ex)
# except:
#     print("Erro desconhecido")
# else:
#     print("Executa quando nenhuma exceção é encontrada")
# finally:
#     print("Mesmo com erro isso é executado")

# criando exceção
class Error(Exception):
    pass

class InputError(Error):
    # toda classe de exceção por convenção termina com Error
    def __init__(self, mensagem):
        self.mensagem = mensagem

# exceção para letras em um input de inteiros
while True:
    # isso vai ser executado pra sempre
    try:
        x = int(input("Entre com um número de 0 a 10: "))
        if x > 10:
            raise InputError("Nota não pode ser maior que 10")
        elif x < 0:
            raise InputError("Nota não pode ser menor que 0")
        # raise força uma exceção
        break
        # isso para o while
    except ValueError:
        print("Valor inválido, este input só aceita números")
    except InputError as ex:
        print(ex)