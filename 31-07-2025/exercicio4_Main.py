from exercicio4 import Pessoa

pessoa1 = Pessoa("João", 20, 70, 1.75)
print(pessoa1, "antes de envelhecer e engordar")
pessoa1.envelhecer()
print(pessoa1, "após envelhecer e crescer")

pessoa1.envelhecer()
print(pessoa1, "após envelhecer")

pessoa1.engordar(5)
print(pessoa1, "após engordar")

pessoa1.emagrecer(3)
print(pessoa1, "após emagrecer")

pessoa1.crescer(0.02)
print(pessoa1, "após crescer")