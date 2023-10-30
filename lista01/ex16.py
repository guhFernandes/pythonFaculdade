#16.	Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado seja apresentado o cargo
#correspondente. Caso o usuário digite um código que não esteja na tabela, mostrar uma mensagem de código inválido.
#Utilize a tabela abaixo:

cod = int(input('Digite um codigo: '))

if cod > 106 or cod < 101:
    print('Codigo invalido')
else:
    if cod == 101:
        print('Vendedor')
    else:
        if cod == 102:
            print('Atendente')
        else:
            if cod == 103:
                print('Auxiliar Técnico')
            else:
                if cod == 104:
                    print('Assistente')
                else:
                    if cod == 105:
                        print('Coordenador de Grupo')
                    else:
                        print('Gerente')



