tempo = float(input("Digite o tempo em que os fundos foram mantidos em depósito: "))

if tempo >= 5:
    print(f"A taxa de juros correspondente a esse tempo é de 0,95!")
else:
    if tempo >= 4:
        print(f"A taxa de juros correspondente a esse tempo é de 0,90!")
    else:
        if tempo >= 3:
            print(f"A taxa de juros correspondente a esse tempo é de 0,85!")
        else:
            if tempo >= 2:
                print(f"A taxa de juros correspondente a esse tempo é de 0,75!")
            else:
                if tempo >= 1:
                    print(f"A taxa de juros correspondente a esse tempo é de 0,65!")
                else:
                    print(f"A taxa de juros correspondente a esse tempo é de 0,55!")