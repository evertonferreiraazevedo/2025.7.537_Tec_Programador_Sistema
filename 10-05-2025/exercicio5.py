import random

numero = []
for i in range(100):
    numero.append(random.randint(1, 6))


print(f"Numero 1: {numero.count(1)}")
print(f"Numero 2: {numero.count(2)}")
print(f"Numero 3: {numero.count(3)}")
print(f"Numero 4: {numero.count(4)}")
print(f"Numero 5: {numero.count(5)}")
print(f"Numero 6: {numero.count(6)}")
