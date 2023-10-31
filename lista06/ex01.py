valor = 4
i = negativos = 0
vetor = []

while i < valor:
    i += 1
    num = int(input(f'Informe o numero {i} para o vetor: '))
    vetor.append(num)

    if num < 0:
        negativos += 1

print(vetor)
print(f'Quantidade de negativos no vetor = {negativos}')

