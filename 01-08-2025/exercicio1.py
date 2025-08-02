class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = True

    def reservar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def liberar(self):
        self.disponivel = True

class Hotel:
    quartos = []

    def __init__(self, nome):
        self.nome = nome

    def reservar_quarto(self, numero):
        for quarto in Hotel.quartos:
            if quarto.numero == numero:
                return quarto.reservar()
        return False

    def liberar_quarto(self, numero):
        for quarto in Hotel.quartos:
            if quarto.numero == numero:
                quarto.liberar()
                return True
        return False

    @classmethod
    def adicionar_quarto(cls, numero, tipo):
        novo_quarto = Quarto(numero, tipo)
        cls.quartos.append(novo_quarto)
        return novo_quarto

    @staticmethod
    def verificar_disponibilidade(numero):
        for quarto in Hotel.quartos:
            if quarto.numero == numero and quarto.disponivel:
                return "Disponível"
        return "Indisponível"

    