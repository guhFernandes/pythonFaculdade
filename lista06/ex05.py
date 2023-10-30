i = soma = 0
vetor = []

quantidade = int(input("Quantidade de posicoes para o vetor: "))
while quantidade < 0:
    quantidade = int(input("Quantidade de posicoes para o vetor: "))

while i < quantidade:
    num = int(input(f'Informe o valor para add na posicao [{i}] do vetor: '))
    while num < 0:
        num = int(input(f'Informe o valor para add na posicao [{i}] do vetor: '))

#   append add um elemento na ultima casa do vetor
    vetor.append(num)
    soma += num
    i += 1

print(f'Valor da soma do vetor e = {soma}')