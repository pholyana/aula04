soma=0
quantidade=int(input("Digite a quantidade de numeros que voce quer a media:"))
for i in range(quantidade):
    num=float(input("Digite um numero"))
    soma=num+soma
media=soma/quantidade
print(media)
