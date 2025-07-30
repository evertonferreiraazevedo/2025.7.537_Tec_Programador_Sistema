#Descrição: Crie uma classe chamada Carro com atributos marca e modelo. Adicione um método chamado descrever que imprime a marca e o modelo do carro. Crie dois objetos dessa classe e chame o método. Crie os métodos fechar_porta e metodo abri_porta.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo    
        self.porta_aberta = False
    def __str__(self):
        return f'{self.marca} - {self.modelo}'
    def abrir_porta(self):
        if self.porta_aberta:
            return f'Porta do {self} já está aberta.'
        self.porta_aberta = True
        return f'Porta do {self} aberta.'
    def fechar_porta(self):
        if not self.porta_aberta:
            return f'Porta do {self} já está fechada.'
        self.porta_aberta = False
        return f'Porta do {self} fechada.'
    
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

while True:
    print("\nCarro 1:", carro1)
    print("Carro 2:", carro2)
    escolha = input("Escolha um carro (1 ou 2) ou 'sair' para encerrar: ")

    if escolha.lower() == 'sair':
        break
    if escolha == '1':
        carro = carro1
    elif escolha == '2':
        carro = carro2 
    else:
        print("Opção inválida. Tente novamente.")
        continue

    print("\nEscolha uma ação:")
    print("1 - Descrever Carro")
    print("2 - Abrir Porta")
    print("3 - Fechar Porta")
    escolha = input("Escolha uma ação: ")

    if escolha == '1':
        print(carro)
    elif escolha == '2':
        print(carro.abrir_porta())
    elif escolha == '3':
        print(carro.fechar_porta())
    else:    
        print("Opção inválida. Tente novamente.")
        continue