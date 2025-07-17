cearense_portugues = {"Abestado": "Bobo",
                   "Batoré": "Baixinho",
                   "Cabra": "Homem",
                   "Celular": "Bebida"
                }

def traducao (palavra):
    if palavra in cearense_portugues:
        print(f"A tradução da palavra {palavra} é {cearense_portugues[palavra]}")
    else:
        print("Palavra não encontrada")

def traducao_inversa(palavra):
    if palavra in cearense_portugues.values():
        for key, value in cearense_portugues.items():
            if value == palavra:
                print(f"A palavra {palavra} é {key}")
                return
while True:
    palavra = input("Qual a palavra deseja traduzir: ")
    traducao(palavra)
    #traducao_inversa(palavra)











