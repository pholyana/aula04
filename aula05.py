neg=0
for i in range(10):
    num=int(input("Digite um numero:"))
    if num <0:
        neg=neg+1
        print(num)
        print(f"encontrei {neg} negativos")

