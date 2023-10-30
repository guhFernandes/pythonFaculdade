# 7.	Escrever a função que recebe por parâmetro uma string e um caracter.
# e a função deve retornar os primeiros caracteres da string até encontrar o
# caracter passado por parâmetro.

i = 0
achei = False

valor_str = input('Informe alguma string: ')
proucurar_str = (input('str proucurar: '))

# len faz a contagem da quantidade de casa de um vetor
while i < len(valor_str) and not achei:

    if proucurar_str == valor_str[i]:
        print(f'{valor_str[i]} = {proucurar_str}')
        achei = True
    else:
        print(f'{valor_str[i]}', end="")
    i += 1
