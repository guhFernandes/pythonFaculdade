# 9.	Implemente uma função que retorne a média
# dos valores armazenados em um vetor de inteiros

vetor = []
stop = "sim"
i = media = 0

while stop == "sim":
    num = int(input("Add valor no vetor: "))
    vetor.append(num)
    stop = input("Deseja add de novo: ")
    while stop != "nao" and stop != "sim":
        stop = input("Deseja add de novo: ")

for i in range(len(vetor)):
    media += (vetor[i] / len(vetor))

if len(vetor) > 0:
    print(f'media = {media}')
else:
    print('divisao por zero nao pode ser feita')
