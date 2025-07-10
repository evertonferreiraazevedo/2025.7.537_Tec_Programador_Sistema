def contar_maiusculas(palavra):
    cont = 0
    for i in palavra:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            cont +=1
    return cont

while True:
    print(f" A palavra tem : {contar_maiusculas(input("Digite uma palavra: "))} letras maiusculas")