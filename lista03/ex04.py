# A prefeitura de uma cidade fez uma pesquisa entre seus
# habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# O final da leitura de dados se dará com a entrada de um salário negativo.

parar = salario = filhos = quantidade_filhos = quantidade_salario = maior_salario = salario_menor_1000 = 0
i = 0
while parar == 0:
    salario = float(input("Informe o salario: "))
    filhos = int(input("Informe a quantidade de filhos: "))

    quantidade_salario += salario
    quantidade_filhos += filhos

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 1000:
        salario_menor_1000 += 1

    i += 1
    parar = int(input("[0] continuar, [-1] parar : "))

print(f"Media de salario = {(quantidade_salario / i):.2f}")
print(f"Media de filhos = {(quantidade_filhos / i):.0f}")
print(f"Maior salario = {maior_salario}")
print(f"Percentual de salarios abaixo de 1000 = {((salario_menor_1000 * 100)/ i):.2f}%")

