cont=0
fora=0
for x in range(10):
    n= int(input("Digite um numero"))
    if n >10 and n <20:
        cont=cont + 1
    else:
        fora=fora + 1

print(f" {fora} Fora do intervalo,{cont} Dentro do intervalo")