# Crie um programa para gerenciar os pedidos de uma lanchonete. O sistema deve simular um menu onde o atendente pode escolher entre as seguintes opções: adicionar um novo pedido, visualizar todos os pedidos ou finalizar o pedido mais antigo. Ao escolher “adicionar pedido”, o atendente deve digitar o nome do cliente junto com o item solicitado (por exemplo: "Ana - X-Burguer"), e essa informação deve ser adicionada à lista de pedidos. Ao escolher “visualizar pedidos”, o programa deve exibir todos os pedidos em ordem, da entrada mais antiga à mais recente. Já ao escolher “finalizar pedido”, o programa deve remover o primeiro item da lista, simulando que esse pedido foi atendido, e exibir qual foi o pedido finalizado. Após cada ação, o programa deve mostrar o estado atualizado da fila de pedidos. O sistema deve continuar funcionando até que o atendente escolha a opção de sair do programa.

opcao = 0
pedido = []
while opcao != 4:
    print("1 - Adicionar pedido")
    print("2 - Visualizar pedidos")
    print("3 - Finalizar pedido")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n")
        
        nome = str(input("Digite o nome do cliente: "))
        item = str(input("Digite o item solicitado: "))
        pedido.append(nome + " - " + item)
        print(f"Pedido adicionado com sucesso! {nome} solicitou {item}")
        print("#"*100)
        print("\n")

    elif opcao == 2:
        print("\n")
        
        print("Pedidos atuais:")
        for i in range(len(pedido)):
            print(f"{i+1} - {pedido[i]}")

        print("#"*100)
        print("\n")
    elif opcao == 3:
        print("\n")
        if pedido:
            pedido_removido = pedido.pop(0)
            print(f"Pedido finalizado: {pedido_removido}")
        else:
            print("Não há pedidos para finalizar.")
        print("#"*100)
        print("\n")
    else:
        print("Obrigado por usar o sistema de gerenciamento de pedidos!")
        print("\n")
        

print("Fim do programa.")


