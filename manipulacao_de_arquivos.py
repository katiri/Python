# abrindo arquivo que já existe ou criando um que não existe
arquivo = open("teste.txt", "w")

# escrevendo no arquivo
arquivo.write("Olá mundo")
arquivo.write("\nOlá mundo 2")

# atualizando arquivo
arquivo = open("teste.txt", "a")

# fechando o arquivo
arquivo.close()

# com funções
def escrever_arquivo(texto):
    arquivo = open("teste.txt", "w")
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open("teste.txt", "a")
    arquivo.write(texto)
    arquivo.close()

escrever_arquivo("teste de escrita")
atualizar_arquivo("\nteste de atualização")

# ler arquivo
arquivo = open("teste.txt", "r")
texto = arquivo.read()
print(texto)

# abrindo arquivo em pasta específica
# arquivo = open("./manipulacao_de_arquivos/teste.txt", "w")
# arquivo.write("teste")

# manipulado notas de alunos em um arquivo
# lista_notas = ["João, 10, 10, 9, 5\n", "Pedro, 10, 10, 9, 5\n", "Luiz, 10, 10, 9, 5\n", "Arthur, 10, 10, 9, 5\n"]
#
# notas = open("notas.txt", "a")
#
# for x in lista_notas:
#     notas.write(x)

lista_medias = []
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    notas_alunos = arquivo.read()
    # split separa uma string em uma lista em elementos separados por um parametro
    notas_alunos = notas_alunos.split("\n")
    for x in notas_alunos:
        dados_aluno = x.split(",")
        aluno = dados_aluno[0]
        dados_aluno.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        print("O aluno", aluno, "teve média", media(dados_aluno))
        lista_medias.append({aluno: media(dados_aluno)})
    return lista_medias

medias = media_notas("notas.txt")
print(medias)

# copiando, movendo e etc arquivos
def copia_arquivos(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, "C:/Desktop/")
    # shutil.move(nome_arquivo, "C:/Desktop/")

copia_arquivos("teste.txt")