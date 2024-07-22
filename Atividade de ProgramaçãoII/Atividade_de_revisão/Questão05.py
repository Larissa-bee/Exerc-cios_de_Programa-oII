#Faça um programa que peça um número inteiro e determine se ele é ou não
#um número primo. Um número primo é aquele que é divisível somente por ele
#mesmo e por 1.

n= int(input("Digite um número inteiro: "))
cont=0
divisor=[]
for i in range(n):
    if n%(i+1)==0:
        cont+=1
        divisor.append(i)
    else:
        cont
if cont==2:
    print("O número é primo")
else:
    print("O número não é primo")





