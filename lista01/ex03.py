nota = int(input('Informe a nota: '))

if nota > 100:
    print('INVALIDA')
else:
    if nota >= 60:
        print('APROVADO')
    else:
        if nota > 0:
            print('REPROVADO')
        else:
            print('INVALIDO')


if nota < 0 or nota > 100:
    print('INVALIDO')
else:
    if nota >= 60:
        print('APROVADO')
    else:
        print('REPROVADO')