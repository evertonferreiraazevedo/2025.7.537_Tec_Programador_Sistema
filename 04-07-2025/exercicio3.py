def contar_vogais(palavra):
    cont = 0 
    for i in palavra:
        if i in 'aeiou':
            cont += 1
    return cont

while True:
    palavra = input("Digite uma palavra: ")
    print(f"A palavra possui: {contar_vogais(palavra)} vogais.")
    if palavra == "sair":
        print("Obrigado")
        break
