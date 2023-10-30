name = input("Digite seu nome: ")
prova1 = float(input("Digite sua nota na primeira prova: "))
prova2 = float(input("Digite sua nota na segunda prova: "))
trabalho = float(input("Digite sua nota no trabalho prova: "))
media = (prova1 * 3) + (prova2 * 5) + (trabalho * 2)


frequencia = int(input("Digite o numero de faltas que voce teve: "))

if frequencia > 15:
    print(f"{name},REPROVADO")
else:
    if media > 60:
        print(f"{name},APROVADO")
    else:
        print(f"{name},FAZER PROVA FINAL")