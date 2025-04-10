num=0
num=0
for i in range(10):
    num=int(input("Digite um numero:"))
    if num <=10 and num >=20:
        num=num+1

else:
    num= 5 - num
print(f" encontrei {num} numeros no intervalo\ne {num} num fora do intervalo")