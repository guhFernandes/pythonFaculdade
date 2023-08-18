print('*'*20 + 'Índice de massa corporal' + '*'*20)

#{:.2f} serve para limitar um valor float

peso = float(input('Informe seu peso "Kg" : '))
altura = float(input('Informe sua altura "m" : '))

imc = peso / (altura * altura)

print('Seu Imc é : {:.2f}' .format(imc))

fim = input()