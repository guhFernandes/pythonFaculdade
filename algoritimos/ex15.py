# 15.	Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

one = int(input('Informe o primeiro numero: '))
two = int(input('Informe o segundo numero: '))
three = int(input('Informe o terceiro numero: '))
four = int(input('Informe o quarto numero: '))

if one < two and one < three and one < four:
    print(f'{one}, é o menor numero')
else:
    if two < one and two < three and two < four:
        print(f'{two}, é o menor numero')
    else:
        if three < one and three < two and three < four:
            print(f'{three}, é o menor numero')
        else:
            print(f'{four}, é o menor numero')


