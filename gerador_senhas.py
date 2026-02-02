import random

# numeros = random.randint(1, 6)

# resultado = str(numeros)
numeros = []

# numeros.append(resultado)

for i in range(6):
    a = random.randrange(1, 6)
    numeros.append(a)

senha = ''

for i in numeros:
    senha = senha + str(i)
    # print(senha)


print(senha)
