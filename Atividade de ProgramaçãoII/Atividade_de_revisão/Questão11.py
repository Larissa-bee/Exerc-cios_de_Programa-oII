#Faça um programa que receba dois números inteiros e gere os números
#inteiros que estão no intervalo compreendido por eles


n1= int(input("Digite um número:"))
n2= int(input("Digite outro número:"))
while n2 <n1:
    n1= int(input("Digite um número: "))
    n2= int(input("Digite outro número: "))
else:
    for i in range(n1,n2+1):
        print(i)
