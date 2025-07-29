class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []  # Notas padrão
    def __str__(self):
        return f"{self.nome} - {self.matricula}"
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    def aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    # def exibir_notas(self):
    #     for i, nota in enumerate(self.notas):
    #         print(f"Nota {i + 1}: {nota}")
    #     return f"{self.nome}, {self.matricula} - Média: {self.calcular_media()}"
    
aluno1 = Aluno("Carlos", "12345")
print(aluno1)
print(aluno1.aprovacao())  # 0.0
aluno1.adicionar_nota(7.5)
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(9.5)
print(aluno1.aprovacao())

# print(aluno1.exibir_notas())
# # print(aluno1.calcular_media())  # 8.0
# aluno1.adicionar_nota(9.0)
# print(aluno1)  # Carlos, 12345 