anterior = 0
atual = 1

for i in range(10):
    print(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo