#Faca um programa que receba do usúario um arquivo texto e mostre na tela quantas ´ letras são vogais.

# try:
#     with open("exemplo2.txt", "r") as arquivo:

#         conteudo = arquivo.read()
#         vogais = 0
#         for letra in conteudo:
#             if letra.lower() in 'aeiou':
#                 vogais += 1
#         print(vogais)

# except FileNotFoundError:
#     print("Arquivo não encontrado")

import os

print("Arquivos disponíveis na pasta:")
for arquivo in os.listdir():
    print(arquivo)
nome_arquivo = input("\nDigite o nome do arquivo que deseja abrir: ").strip()

try:
    with open("nome_arquivo", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        vogais = 0
        for letra in conteudo:
            if letra.lower() in 'aeiou':
                vogais += 1
        print(f"\nO arquivo '{nome_arquivo}' contém {vogais} vogais.")


except FileNotFoundError:
    print("\nArquivo não encontrado. Verifique o nome e tente novamente.")

except Exception as e:
    print(f"Erro ao abrir o arquivo: {e}")
