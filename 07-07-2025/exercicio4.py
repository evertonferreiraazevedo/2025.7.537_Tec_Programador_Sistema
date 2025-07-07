def entrada_dados():
    #retorna o valor do input do usuario
    return int(input("Digite um numero: "))
def soma(n1, n2, n3):
    #printar a soma dos numero recebidos
    print(f"A soma dos numeros é: {n1 + n2 + n3}")

#Codigo principal
#atribuindo o valor das variaveis usando o retorno da função
numero1 = entrada_dados()
numero2 = entrada_dados()
numero3 = entrada_dados()

#calculando soma dos numero passando como parametro
soma(numero1, numero2, numero3)