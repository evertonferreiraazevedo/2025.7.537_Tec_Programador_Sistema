estoque = []

while True:
    print("\nMenu - Controle de Estoque")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Vender produto")
    print("4. Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ").strip()
        try:
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            if quantidade < 0 or preco < 0:
                raise ValueError
            produto = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
            estoque.append(produto)
            print(f"Produto '{nome}' adicionado ao estoque!")
        except ValueError:
            print("Erro: Quantidade e preço devem ser números positivos.")

    elif opcao == "2":
        if not estoque:
            print("Estoque vazio.")
        else:
            for p in estoque:
                print(f"Produto: {p['nome']} – Quantidade: {p['quantidade']} – Preço: R$ {p['preco']:.2f}")

    elif opcao == "3":
        nome_venda = input("Digite o nome do produto a vender: ").strip()
        try:
            qtd_venda = int(input("Digite a quantidade a vender: "))
            encontrado = False

            for p in estoque:
                if p['nome'].lower() == nome_venda.lower():
                    encontrado = True
                    if p['quantidade'] >= qtd_venda:
                        p['quantidade'] -= qtd_venda
                        print(f"Venda realizada: {qtd_venda} unidades de {p['nome']}")
                    else:
                        print("Estoque insuficiente.")
                    break

            if not encontrado:
                print("Produto não encontrado no estoque.")
        except ValueError:
            print("Erro: Quantidade inválida. Tente novamente.")

    elif opcao == "4":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
