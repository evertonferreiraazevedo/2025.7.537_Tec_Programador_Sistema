contatos = {}
nome_valido = False
telefone_valido = False 

while True:
    print("\nMenu - Agenda de Contatos")
    print("1. Adicionar novo contato")
    print("2. Listar todos os contatos")
    print("3. Sair do programa")

    opcao = input("Escolha uma opção: ")

    
    if opcao == "1":
        while True:
            try:
                nome = input("Digite o nome do contato: ").strip()
                telefone = input("Digite o telefone (formato 99999-9999): ").strip()

                if nome == "" or telefone == "":
                    print("Erro: Nome e telefone não podem estar vazios.")
                    continue

                for i in telefone:
                    if i not in "0123456789-":
                        raise ValueError("Telefone contém caracteres inválidos")

                contatos[nome] = telefone
                print(f"Contato '{nome}' adicionado com sucesso!")
                break

            except ValueError as e:
                print(f"Erro: {e}")
                continue


    elif opcao == "2":
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            for nome, telefone in contatos.items():
                print(f"Nome: {nome} – Telefone: {telefone}")

    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
