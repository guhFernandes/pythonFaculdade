horas_trabalhadas = int(input("Digite o número de horas que você trabalha por semana: "))

if horas_trabalhadas <= 40:
    print(f'Seu salário = {horas_trabalhadas * 15} reais!')
else:
    print(f'Seu salário = {(horas_trabalhadas - 40) * 21 + 600} reais!')