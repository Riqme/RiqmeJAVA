notass = []
soma_notas = 0

for i in range(5):
    notas = input('Digite a nota {}:'. format(i + 1))
    notass.append(notas)

for i in notass:
    if (i % 2 == 0):
        soma_notas = soma_notas + i

print('A soma das notas pares são: {}'.format(soma_notas))