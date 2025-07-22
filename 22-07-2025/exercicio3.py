#Faça um programa que receba do usuario um arquivo texto. Crie outro arquivo texto ´ contendo o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’.

def ler_arquivo():
    try:
        with open('exemplo.txt', 'r') as arquivo:
            texto = arquivo.read()
            return texto
    except:
        return "Arquivo nao encontrato"

def substituir_vogais(texto):
    vogais = 'aeiouAEIOU'
    for vogal in vogais:
        texto = texto.replace(vogal, '*')
    return texto

def preencher_arquivo(conteudo):
    try:
        with open('exemplo2.txt', 'w') as arquivo:
            arquivo.write(conteudo)
            return "Arquivo alterado com sucesso"
    except:
        return "Arquivo nao pode ser escrito"


print(preencher_arquivo(substituir_vogais(ler_arquivo())))
