# 6.	Construir um algoritmo que calcule a média aritmética
# de vários valores inteiros positivos, digitados pelo usuário.
# O final da leitura acontecerá quando for lido um valor
# negativo.

soma = 0
quantidade = 0
valor = int(input("Digite um valor: "))
while valor >= 0:
    soma = soma + valor
    quantidade = quantidade + 1
    valor = int(input("Digite um valor: "))

if quantidade > 0:
    print(f"Média = {soma / quantidade:.2f}")
