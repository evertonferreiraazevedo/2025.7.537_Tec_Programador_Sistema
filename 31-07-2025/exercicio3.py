class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return f"Retângulo(base={self.base}, altura={self.altura})"
    
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def verificar_base(self):
        return self.base
    
    def verificar_altura(self):
        return self.altura
  
    def mudar_base(self, nova_base):
        self.base = nova_base
   
    def mudar_altura(self, nova_altura):
        self.altura = nova_altura