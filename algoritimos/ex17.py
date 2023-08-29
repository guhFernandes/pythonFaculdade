# 17.	Uma encomenda de unidades de disco contém unidades marcadas com um código de 1 a 4, que indica o tipo seguinte:
# Código 	Tipo da unidade
# 1   	CD-ROM (700MB)
# 2   	DVD-ROM (4.7GB)
# 3   	DVD-9 (8.54 GB)
# 4   	Blu-Ray (25 GB)

# Escreva um programa que receba o número de um código como entrada e, baseado no valor digitado, informe o tipo correto de unidade de disco.

cod = int(input('Digite um codigo: '))

if cod > 4 or cod < 1:
    print('Codigo invalido')
else:
    if cod == 1:
        print('CD-ROM (700MB)')
    else:
        if cod == 2:
            print('DVD-ROM (4.7GB)')
        else:
            if cod == 3:
                print('DVD-9 (8.54 GB)')
            else:
                print('Blu-Ray (25 GB)')
