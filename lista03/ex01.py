# 1.	Escrever um algoritmo que lê 10 valores e conte
# quantos destes valores são negativos, escrevendo esta informação

positivo = negativo = 0

for i in range (1, 10 + 1):
    num = int(input(f"Numero {i} informe seu valor: "))

    if num >= 0:
        positivo += 1
    else:
        negativo += 1

print(f"Positivos igual = {positivo}")
print(f"Negativos igual = {negativo}")