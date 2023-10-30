# 2.	Escreva um algoritmo que leia 20 valores e encontre
# o maior e o menor deles. Mostre o resultado

maior = menor = 0

for i in range(1, 5 + 1):
    num = int(input(f"Informe o valor {i}: "))

    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"Maior = {maior}")
print(f"Menor = {menor}")
