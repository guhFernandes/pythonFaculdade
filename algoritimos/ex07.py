salario = int(input('Informe o salario: '))
anoCasa = int(input('Informe o tempo de casa(em anos): '))

if anoCasa <=1 :
    print(salario*1.1)
else:
    print(salario*1.2)