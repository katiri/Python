# terminal:
# pip install nome_do_pacote: instala pacote
# pip uninstall nome_do_pacote: desinstala pacote
# pip freeze: lista pacotes instalados
# pip list: lista todos os pacotes

from requests import *
# requisição do via cep
response = get("https://cardapioz.com.br")
print(response.status_code)
print(response.text)
# print(response.json())
# dados_cep = response.json()
# print(dados_cep["logradouro"])