#criar lista
#preencher lista com inputs de um usuario (use um for)
#use len(lista) para descobrir quantidades de elementos
#use sun(lista) para somar todos os elementos
#calcule media
#imprimir media
#use for para percorrer a lista e da append em cada elemento 
#maior que media

temperaturas = []
temperaturas_maior_que_media = []
for i in range(5):
    temperatura = float(input(f"Digite a temperatura {i+1}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
print(f"Media: {media}")

for i in range(len(temperaturas)):
    if temperaturas[i] > media:
        temperaturas_maior_que_media.append(temperaturas[i])

print(f"Temperaturas maiores que a media: {temperaturas_maior_que_media}")