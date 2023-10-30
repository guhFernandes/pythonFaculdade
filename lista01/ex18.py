# 18.	Escreva um programa que receba dois números reais e um código de seleção do usuário.
# Se o código digitado for 1, faça o programa adicionar os dois números previamente digitados
# e mostrar o resultado; se o código de seleção for 2, os números devem ser multiplicados; se
# o código de seleção for 3, o primeiro número deve ser dividido pelo segundo. Se nenhuma das opções
# acima for escolhida, mostrar "Código inválido".

print('****Cods****')
print('1 = somar')
print('2 = multi')
print('3 = divi')

print('')

numRealsOne = float(input('Informe o primeiro numero: '))
numRealsTwo = float(input('Informe o segundo numero: '))
cod = int(input('Informe o codigo: '))

if cod > 3 or cod < 1:
    print('Codigo invalido!!')
else:
    if cod == 1:
        print(f'A soma de {numRealsOne} + {numRealsTwo} = {numRealsOne + numRealsTwo}')
    else:
        if cod == 2:
            print(f'O produto de {numRealsOne} * {numRealsTwo} = {numRealsOne * numRealsTwo}')
        else:
            print(f'A divisao de {numRealsOne} / {numRealsTwo} = {numRealsOne / numRealsTwo}')

