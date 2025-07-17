estoque = {
    "camiseta": 10,
    "calça": 5,
    "jaqueta": 8,
    "sapato": 12
}

while True:
    produto = input("Insira o nome do produto: ").lower()
    if produto in estoque:
        print(f"Quantidade em estoque: {estoque[produto]}")
    else:
        print("Produto não está disponível.")
