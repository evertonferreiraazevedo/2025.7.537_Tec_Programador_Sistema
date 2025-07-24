import json
def carregar_dados():
    try:
        with open('produtos.json', 'r', encoding='utf-8') as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []

def salvar_dados(lista):
    with open('produtos.json', 'w', encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4)

def cadastrar_produto():
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    produto = {'nome': nome, 'preco': preco}
    lista = carregar_dados()
    lista.append(produto)
    salvar_dados(lista)
    print('Produto cadastrado!')

def listar_produtos():
    lista = carregar_dados()
    if lista:
        for p in lista:
            print(f"{p['nome']} - R$ {p['preco']:.2f}")
    else:
        print('Nenhum produto cadastrado.')

def apagar_produto():
    nome = input('Nome do produto a ser apagado: ')
    lista = carregar_dados()
    for p in lista:
        if p['nome'] == nome:
            lista.remove(p)
            salvar_dados(lista)
            print('Produto apagado!')
            return
    print('Produto não encontrado.')

def atualizar_produto():
    nome = input('Nome do produto a ser atualizado: ')
    lista = carregar_dados()
    for p in lista:
        if p['nome'] == nome:
            novo_nome = input('Novo nome do produto: ')
            novo_preco = float(input('Novo preço do produto: '))
            p['nome'] = novo_nome
            p['preco'] = novo_preco
            salvar_dados(lista)
            print('Produto atualizado!')
            return
    print('Produto não encontrado.')

def menu():
    while True:
        print('1 - Cadastrar produto')
        print('2 - Listar produtos')
        print('3 - Sair')
        opcao = input('Escolha: ')
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            apagar_produto()
        elif opcao == '4':
            atualizar_produto()
        elif opcao == '5':
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    menu()