print("Bem vindo a calculadora em Python!")
operador = "" 
print("Digite dois numero e logo apos a operação desejada ou digite 'sair' para sair: ")
while operador != "sair":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operador = input("Escolha uma das operações abaixo: " \
    "\n 1 - soma " \
    "\n 2 - subtração " \
    "\n 3 - multiplicação " \
    "\n 4 - divisão " \
    "\n 5 - potência " \
    "\n 6 - modulo: "\
    "\n ou digite 'sair' para sair: ")
    
    if operador == "1":
        print("A soma dos dois números é: ", num1 + num2)
    elif operador == "2":
        print("A subtração dos dois números é: ", num1 - num2)
    elif operador == "3":
        print("A multiplicação dos dois números é: ", num1 * num2)
    elif operador == "4":
        print("A divisão dos dois números é: ", num1 / num2)
    elif operador == "5":
        print("A potência do primeiro número é: ", num1 ** num2)
    elif operador == "6":
        print("O módulo do primeiro número é: ", num1 % num2)
    elif operador == "sair":
        print("Obrigado por usar a calculadora em Python!")
    else:
        print("Operador inválido. Por favor, escolha uma das opções acima.")