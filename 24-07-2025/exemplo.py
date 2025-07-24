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
            break
        else:
            print('Opção inválida.')

menu()