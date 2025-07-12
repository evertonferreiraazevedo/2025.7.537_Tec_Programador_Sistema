# Durante uma semana, foram registradas as temperaturas corporais de um paciente: [36.8, 37.5, 38.2, 37.0, 36.5, 39.1, 38.6].  Crie um programa que exiba apenas as temperaturas consideradas febre (acima de 37.5ºC).

temp = [36.8, 37.5, 38.2, 37.0, 36.5, 39.1, 38.6]
print(temp)

tamanho_lista = len(temp)
for i in range(tamanho_lista):
    if temp[i] > 37.5:
        print(f"A temperatura {temp[i]} é maior que 37,5")
   