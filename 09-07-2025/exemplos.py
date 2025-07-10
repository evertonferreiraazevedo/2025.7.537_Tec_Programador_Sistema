numeros = [-1,-2,-3,-4,-5,-6]
pessoas = ["Eu", "Tu", "Ele", "Nós", "Vós", "Eles"]
misturado = [1, "eu", 2 , "tu"]

print(numeros)
print(pessoas)
print(misturado)

numeros[0]= "Zezinho"

print(numeros)

numeros[-2: -1] = ["huguinho", "luizinho"]
print(numeros)

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print("Tamanho da lista:", len(lista)) # Saída: Tamanho da lista: 10

print("Soma dos elementos:", sum(lista)) # Saída: Soma dos elementos: 39

print("Menor elemento:", min(lista)) # Saída: Menor elemento: 1

print("Maior elemento:", max(lista)) # Saída: Maior elemento: 9

print("Lista ordenada:", sorted(lista)) # Saída: Lista ordenada: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

lista_palavras = ["banana", "abacaxi", "laranja", "uva", "maçã"]

# Utilizando todas as funções dentro do print
print("Tamanho da lista:", len(lista_palavras), 
   "\nLista de palavras:", lista_palavras,
   "\nMenor palavra (lexicograficamente):", min(lista_palavras), 
   "\nMaior palavra (lexicograficamente):", max(lista_palavras), 
   "\nLista ordenada:", sorted(lista_palavras))

lista = [1, 2, 3, 4, 5]
print(lista)

# Adicionando elementos com .append(), .insert() e .extend()
lista.append(6) # adiciona 6 ao final da lista
print(lista)
lista.insert(1, 10) # insere 0 na posição 0
print(lista)
lista.extend([7, 8, 9, 5]) # adiciona os elementos 7, 8, 9 ao final da lista
print(lista)

# Removendo elementos com .remove(), .pop() e .clear()
lista.remove(5) # remove o elemento 5
print(lista)
elemento_removido = lista.pop(2) # remove o elemento na posição 2 e retorna o valor removido
print(lista)
print(elemento_removido)
lista.clear() # limpa a lista completamente
print(lista)


lista = [1, 2, 3, 4, 5,6,7,2,4,2,7,10,12]

# Usando .index() para buscar o índice do primeiro elemento igual a 2
print("Índice do primeiro '2' na lista:", lista.index(2))
print(lista)

# Usando .count() para contar quantas vezes o elemento 2 aparece na lista
print("Número de vezes que '2' aparece na lista:", lista.count(2))
print(lista)

