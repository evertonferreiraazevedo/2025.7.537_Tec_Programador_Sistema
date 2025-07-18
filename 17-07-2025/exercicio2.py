produtos = {}

while True:
    print("\nMenu - Cadastro de Produtos")
    print("1. Cadastrar novo produto")
    print("2. Mostrar todos os produtos cadastrados")
    print("3. Encerrar o programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ").strip()
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco < 0:
                raise ValueError
            produtos[nome] = preco
            print(f"Produto '{nome}' cadastrado com sucesso!")
        except ValueError:
            print("Erro: Preço inválido. Tente novamente.")

    elif opcao == "2":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for nome, preco in produtos.items():
                print(f"Produto: {nome} – Preço: R$ {preco:.2f}")

    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
