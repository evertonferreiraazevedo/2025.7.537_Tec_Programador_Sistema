pacientes = []

while True:
    print("\nMenu - Clínica Médica")
    print("1. Cadastrar novo paciente")
    print("2. Buscar paciente por CPF")
    print("3. Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do paciente: ").strip()
        try:
            idade = int(input("Digite a idade: "))
            cpf = input("Digite o CPF: ").strip()

            if not nome or idade < 0 or not cpf:
                raise ValueError

            paciente = {'nome': nome, 'idade': idade, 'cpf': cpf}
            pacientes.append(paciente)
            print("Paciente cadastrado com sucesso!")
        except ValueError:
            print("Erro: Dados inválidos. Tente novamente.")

    elif opcao == "2":
        cpf_busca = input("Digite o CPF para busca: ").strip()
        encontrado = False
        for p in pacientes:
            if p['cpf'] == cpf_busca:
                print(f"Nome: {p['nome']}, Idade: {p['idade']}, CPF: {p['cpf']}")
                encontrado = True
                break
        if not encontrado:
            print("Paciente não encontrado.")

    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
