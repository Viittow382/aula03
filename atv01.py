nome =  input("Digite seu nome")
idade = int (input ("digite sua idade"))
salario = float(input("Digite seu salario"))
percentual=float(input("digite o percentual"))

valoraumento = salario*percentual/100
novosalario = salario+valoraumento
print(f"olá {nome}voce tem {idade} anos, seu salario atual é {salario}, voce teve {percentual} de aumento e seu novo salario será{valoraumento: .2f}" )