salario = float(input("Digite aqui seu salario: "))
financiamento = float(input("Digite aqui o valor do financiamento: "))

variavel_imprestimo = salario * 5

if financiamento <= variavel_imprestimo:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")