class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"


pessoa1 = Pessoa("João", 30)
print(pessoa1.__str__())

pessoa2 = Pessoa("Maria", 25)
print(f"A primeira pessoa é {pessoa1.nome},e ela possui {pessoa1.idade} anos")