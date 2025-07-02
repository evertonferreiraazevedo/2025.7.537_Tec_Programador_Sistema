import random
# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)
print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 10. Tente adivinhar!")
acertou = False
while not acertou:
  # Solicita um palpite do usuário
  palpite = int(input("Digite o seu palpite: "))
    # Verifica se o palpite está correto
  if palpite < numero_secreto:
    print("O número é maior. Tente novamente.")
  elif palpite > numero_secreto:
    print("O número é menor. Tente novamente.")
  else:
    print("Parabéns! Você acertou o número!")
    acertou = True

