class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        if self.idade < 21:
            self.crescer(0.05)
        self.idade += 1
    def engordar(self, kilos):
        self.peso += kilos
    def emagrecer(self, kilos):
        self.peso -= kilos
    def crescer(self, centimetros):
        self.altura += centimetros
    def __str__(self):
        return f"Pessoa nome: {self.nome}, idade: {self.idade}, peso: {self.peso}, altura: {self.altura}"
    
