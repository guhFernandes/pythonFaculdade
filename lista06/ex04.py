vetor = [1, 8, 4, 9, 7, -1]

def ordernar(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[i] > vetor[j]:
                aux = vetor[j]
                vetor[j] = vetor[i]
                vetor[i] = aux
    
    return vetor


print( ordernar(vetor) )

