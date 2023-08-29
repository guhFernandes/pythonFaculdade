ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano que voce nasceu: "))
idade = ano_atual - ano_nascimento
print(f"Voce tem {idade} anos!")

if idade > 64:
    print("idosa")
else:
    if idade >= 18:
        print("adulta")
    else:
        if idade >= 12:
            print("adolescente")
        else:
            if idade >= 4:
                print("criança")
            else:
                print("bebê")