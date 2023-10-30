# 3.	Faça um algoritmo que lê um valor N
# inteiro e positivo e que calcula e escreve o fatorial de N (N!).

num = int(input("Informe o valor a calcualar: "))
fatorial = 1
if num > 0:

    for i in range(1, num + 1):
        fatorial = (fatorial * i)
else:
    print("Numero invalido")

print(f"{num}!= {fatorial}")