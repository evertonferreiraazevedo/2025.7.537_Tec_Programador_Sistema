class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.criticas = 0  # Críticas padrão
    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.ano}'
    def reputacao(self):
        if self.criticas > 8:
            return "Clássico"
        elif self.criticas > 5:
            return "Mediano"
        else:
            return "Ruim"

livro1 = livro("Dom Casmurro", "Machado de Assis", 1899)
print(livro1)  # Saída: Dom Casmurro - Machado de Assis - 1899
print(livro1.reputacao())  # Saída: Ruim
livro1.criticas = 9
print(livro1.reputacao())  # Saída: Clássico
