opcao = ""
fila = []
ultimo_numero = 0

while opcao != "3": 
    print("\nOpções:")
    print("1 - Gerar nova senha")
    print("2 - Chamar próximo da fila")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ultimo_numero += 1 
        fila.append(ultimo_numero)
        print(f"Sua senha gerada é: {ultimo_numero}")
    
    elif opcao == "2":
        if fila:
            senha = fila.pop(0) 
        else:
            senha = "Fila vazia!"
        print(f"Senha chamada: {senha}")
    
    elif opcao == "3":
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")
