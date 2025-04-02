quantidade= float(input("Digite a quantidade do combustivel "))
tipo= input("digite o tipo de combustivel abastecido ")
if tipo=="E" or tipo=="e":
    valor=quantidade*4.9
    print(f"quantidade abastecido {quantidade} valor a pagar {valor:.2f}: ")
else:
    if tipo=="G" or tipo=="g":
        valor=quantidade*5.8
        print(f"quantidade abastecido {quantidade} valor a pagar {valor:.2f}: ")
    else:
        print(f"tipo de combustivel invalido")


