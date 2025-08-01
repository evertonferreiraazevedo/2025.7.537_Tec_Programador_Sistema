class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def verificar_lado(self):
        return self.lado

    @staticmethod
    def area(lado):
        return lado ** 2

quadrado = Quadrado(5)
print(Quadrado.area(quadrado.lado))  # Output: 25
print(quadrado.verificar_lado())  # Output: 5
quadrado.mudar_lado(10)
print(quadrado.verificar_lado())  # Output: 10
print(Quadrado.area(quadrado.lado)) # Output: 100