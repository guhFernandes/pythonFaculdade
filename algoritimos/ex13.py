ano = int(input("Digite o ano do modelo do seu carro: "))
peso = float(input("Digite o peso do seu carro em kg: "))


if ano <= 1970 and peso < 1200:
    print("Classe 1 e Taxa de Registro de 16,50")
else:
    if ano <= 1970 and peso <= 1700:
        print("Classe 2 e Taxa de Registro de 25,50")
    else:
        if ano <= 1970 and peso > 1700:
            print("Classe 3 e Taxa de Registro de 46,50")
        else:
            if ano <= 1979 and peso < 1200:
                print("Classe 4 e Taxa de Registro de 27,00")
            else:
                if ano <= 1979 and peso <= 1700:
                    print("Classe 5 e Taxa de Registro de 30,50")
                else:
                    if ano <= 1979 and peso > 1700:
                        print("Classe 6 e Taxa de Registro de 52,50")
                    else:
                        if ano >= 1980 and peso < 1600:
                            print("Classe 7 e Taxa de Registro de 19,50")
                        else:
                            print("Classe 8 e Taxa de Registro de 55,50")