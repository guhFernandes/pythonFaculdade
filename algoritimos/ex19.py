# 19.	Faça um algoritmo que transforme a nota de um aluno em conceito.
# As notas 10 e 9 receberão conceito A, as notas 8 e 7 receberão conceito B,
# as notas 6 e 5 receberão conceito C e abaixo de 5 conceito D.

nota = float(input('Informe a nota: '))

if nota > 10 or nota < 0:
    print('Nota invalida!')
else:
    if nota >= 9:
        print('Conceito A')
    else:
        if nota >= 7:
            print('Conceito B')
        else:
            if nota >= 5:
                print('Conceito C')
            else:
                print('Conceito D')
