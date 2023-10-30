from random import randint

# 8 Implemente uma função que, dado um valor,
# retorne se esse valor pertence ou não a um vetor de inteiros.

verifica = False
vetor = []
i = j = achei = 0

while i < 10:
    i += 1
    vetor.append(randint(1, 100))

valor_busca = int(input('Valor a ser buscado no vetor: '))

while not verifica and j < len(vetor):
    if valor_busca == vetor[j]:
        achei = vetor[j]
        verifica = True
    j += 1

if not verifica:
    print('valor nao pertence ao vetor')
else:
    print('Valor pertence ao vetor')