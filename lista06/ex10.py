# 10.	Escrever uma função que substitui por zero
# todos os números negativos do vetor passado por parâmetro.

vetor = []
stop = "sim"

while stop == "sim":
    num = int(input("Add valor no vetor: "))
    vetor.append(num)
    stop = input("Deseja add de novo: ")
    while stop != "nao" and stop != "sim":
        stop = input("Deseja add de novo: ")


print(f"Vetor antigo: {vetor}")
for i in range(len(vetor)):
    if vetor[i] < 0:
        vetor[i] = 0
print(f"Vetor novo: {vetor}")
