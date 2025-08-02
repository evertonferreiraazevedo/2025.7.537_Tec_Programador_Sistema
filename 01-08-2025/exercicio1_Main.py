from exercicio1 import Hotel

hotel = Hotel("Hotel Central")

Hotel.adicionar_quarto(101, "simples")
Hotel.adicionar_quarto(102, "duplo")
Hotel.adicionar_quarto(103, "suite")

# print(Hotel.verificar_disponibilidade(101)) 

print(hotel.reservar_quarto(101))
print(hotel.reservar_quarto(101))

print(Hotel.verificar_disponibilidade(101))  


# hotel.liberar_quarto(101)
# print(Hotel.verificar_disponibilidade(101)) 