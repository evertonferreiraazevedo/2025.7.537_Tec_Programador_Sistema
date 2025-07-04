preco_pao = float(input("Preço do pão: R$ "))
print("Panificadora Pão de Ontem - Tabela de preços")

i = 1

while i <= 50:
    preco_total = i * preco_pao  
    print(f"{i} - R$ {preco_total:.2f}")
    i += 1  
