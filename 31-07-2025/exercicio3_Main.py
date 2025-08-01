import exercicio3

base_sala = float(input("Digite a base  da sala: "))
altura_sala = float(input("Digite a altura da sala: "))
retangulo_Sala = exercicio3.Retangulo(base_sala, altura_sala)

base_piso = float(input("Digite a base  da sala: "))
altura_piso = float(input("Digite a altura da sala: "))
retangulo_Piso = exercicio3.Retangulo(base_piso, altura_piso)

quantidade_pisos = retangulo_Sala.area() / retangulo_Piso.area()
quantidade_rodape = retangulo_Sala.perimetro() / retangulo_Piso.verificar_base()

print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
print(f"Quantidade de rodapé necessário: {quantidade_rodape:.2f}")


# print(f"Retângulo criado: {retangulo}")
# print(f"Área do retângulo: {retangulo.area()}")
# print(f"Perímetro do retângulo: {retangulo.perimetro()}")
                                 
# print(f"Base do retângulo: {retangulo.verificar_base()}")
# print(f"Altura do retângulo: {retangulo.verificar_altura()}")
# retangulo.mudar_altura(5)
# retangulo.mudar_base(5)

# print(f"Novo valor Base do retângulo: {retangulo.verificar_base()}")
# print(f"Novo valor Altura do retângulo: {retangulo.verificar_altura()}")
# print(f"Nova Área do retângulo: {retangulo.area()}")
# print(f"Novo Perímetro do retângulo: {retangulo.perimetro()}")