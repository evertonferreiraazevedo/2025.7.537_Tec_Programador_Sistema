populacaoA = int(input("População do país A: "))

while populacaoA < 0:
    populacaoA = int(input("População do país deve ser maior que 0: "))

taxaA = float(input("Taxa de crescimento da cidade A: "))

populacaoB = int(input("População do país B: "))
while populacaoB < 0:
    populacaoB =int(input("População do país deve ser maior que 0: "))

taxaB = float(input("Taxa de crescimento da cidade B: "))

ano = 0
while populacaoA < populacaoB:
    ano += 1
    populacaoA = int((1 + (taxaA/100) )* populacaoA)
    populacaoB = int((1 + (taxaB/100) )* populacaoB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % populacaoA)
    print("População B: %d\n\n" % populacaoB)

print("Ultrapassa no ano:",ano)