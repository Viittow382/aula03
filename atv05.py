nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
nota3 = float(input("Digite a terceira nota"))

media= (nota1+nota2+nota3)/3

if media >=7:
    print(f"Aprovado: {media}")

else :
    if media>=7:
        print("Aprovado")
    else:
        if media<4:
            print("reprovado")
        else:
            print(f"reprovado:{media}")

    
