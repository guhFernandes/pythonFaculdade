# 20.	Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos,
# calcule e imprima: a média dos números caso a soma deles for menor que 8, seu produto
# caso a soma seja igual a 8 ou a divisão do maior pelo menor caso a soma dos valores for maior que 8.

print('Valores entre 1 e 10')

numberOne = int(input("Digite o primeiro valor: "))
numberTwo = int(input("Digite o segundo valor: "))

soma = numberOne + numberTwo

if numberOne > 10 or numberOne < 1 or numberTwo > 10 or numberTwo < 1:
    print('Valor Invalido!!')
else:
    if soma < 8:
        print(f'A media de {numberOne} + {numberTwo} = {soma / 2} ')
    else:
        if soma == 8:
            print(f'O produto de {numberOne} * {numberTwo} = {numberOne * numberTwo}')
        else:
            if numberOne > numberTwo:
                print(f'A divisao de {numberOne} / {numberTwo} = {numberOne / numberTwo}')
            else:
                print(f'A divisao de {numberTwo} / {numberOne} = {numberTwo / numberOne}')
