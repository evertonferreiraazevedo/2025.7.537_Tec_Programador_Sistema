def eh_primo(numero):
    cont = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            cont +=1
        else:
            cont+1
    if cont == 2:
        return True
    else:
        return False


# print(eh_primo(10))

for i in range(100):
    if eh_primo(i):
        print(i)

