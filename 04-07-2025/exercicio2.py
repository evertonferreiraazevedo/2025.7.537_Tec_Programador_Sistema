def calc_media(n1, n2, n3, n4): 
    return (n1 + n2 + n3 + n4) / 4

while True:
    n1 = int(input("Digite a nota: "))
    n2 = int(input("Digite a nota: "))
    n3 = int(input("Digite a nota: "))
    n4 = int(input("Digite a nota: "))
    print(f"Media das notas: {calc_media(n1, n2, n3 , n4)}\n\n")  
