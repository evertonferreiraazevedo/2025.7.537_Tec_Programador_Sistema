# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def __str__(self):
#         return f"{self.nome}, {self.idade} anos"

# pessoa1 = Pessoa("João", 30)
# pessoa2 = Pessoa("Maria", 25)
# print(pessoa1)
# print(pessoa2)
# print(f"A primeira pessoa é {pessoa1.nome},e ela possui {pessoa1.idade} anos")
# print(f"A segunda pessoa é {pessoa2.nome},e ela possui {pessoa2.idade} anos")
# print(pessoa1)
# print(pessoa2)

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.raca = "SRD"  # Raça padrão     
    def latir(self):
        return f"{self.nome}, {self.idade} anos"

cachorro1 = Cachorro("Caramelo", 5 )
cachorro1.raca = "Labrador"
print(cachorro1.latir() + f" e é da raça {cachorro1.raca}")

cachorro2 = Cachorro("Mel", 3)
print(cachorro2.latir() + f" e é da raça {cachorro2.raca}")

