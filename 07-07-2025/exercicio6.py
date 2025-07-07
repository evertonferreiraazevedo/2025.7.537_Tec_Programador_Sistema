def contar_digitos(numero):
    if numero == 0:
        return 1  # zero tem 1 dígito

    elif numero < 0:
        numero *= -1
    contador = 0
    while numero > 0:
        numero = numero // 10
        print(numero)
        contador += 1
    return contador

def contar_digitos_sem_trabalho(numero):
    return len(str(numero))

numero = int(input("Digite um numero: "))
print(f"Digitos : {contar_digitos(numero)}")
print(f"Digitos do modo facil: {contar_digitos_sem_trabalho(numero)}")