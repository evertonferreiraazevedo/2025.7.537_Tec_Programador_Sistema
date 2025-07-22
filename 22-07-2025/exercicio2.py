#Faca um programa que receba do usuario um arquivo texto e um caracter. Mostre na tela ´ quantas vezes aquele caractere ocorre dentro do arquivo


def contar_elemento(letra):
    try:
        with open("exemplo.txt", 'r') as arquivo:
            conteudo = arquivo.read()
            print(f"A letra {letra} aparece {conteudo.count(letra)} vezes no arquivo {arquivo.name}")
            for i in conteudo:
                if i == letra:
                    cont += 1
            print(f"A letra {letra} aparece {cont} vezes no arquivo {arquivo.name}")    

    except FileNotFoundError:
        print("Arquivo não encontrado")



letra = input("Qual letra voce deseja buscar? ").lower()
cont = 0
contar_elemento(letra)

