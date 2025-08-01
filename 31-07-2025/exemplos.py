# class Carro:
#     rodas = 4   # Atributo de classe
#     def __init__(self, ano, modelo):
#         self.ano = ano  # Atributo de instância
#         self.modelo = modelo  # Atributo de instância
     
# carro1 = Carro(1980, "Fusca")
# print(carro1.ano)  # Acesso ao atributo de instância
# print(carro1.modelo)  # Acesso ao atributo de instância
# print(carro1.rodas)  # Acesso ao atributo de classe

class Pessoa:
    populacao = 0  # atributo de classe
    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1
    
    @classmethod
    def mostrar_populacao(cls):
        print(f"População total: {cls.populacao}")

p1 = Pessoa("Ana")
p2 = Pessoa("João")
Pessoa.mostrar_populacao()  # Saída: População total: 2

for i in range(3000):
    p = Pessoa(f"Pessoa {i+1}")

Pessoa.mostrar_populacao()

# class Calculadora:

#     @staticmethod
#     def somar(a, b):
#         return a + b
    
#     @classmethod
#     def subtrair(cls, a, b):
#         return a - b
    
#     def multiplicar(self, a, b):
#         return a * b
    
# print(Calculadora.somar(10, 5))
# print(Calculadora.subtrair(10, 5))
# calc = Calculadora()
# print(calc.multiplicar(10, 5))