class Bola:
    def __init__(self, cor, diametro, material):
        self.cor = cor 
        self.tamanho = diametro
        self.material = material
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        return self.cor
    def mostrar_cor(self):
        return self.cor
    @staticmethod
    def calcular_area(diametro):
        return 3.14 * (diametro / 2) ** 2
    
bola = Bola("vermelha", 30, "borracha")
print(bola.mostrar_cor())
print(bola.trocar_cor("azul"))  
print(Bola.calcular_area(bola.tamanho))   

