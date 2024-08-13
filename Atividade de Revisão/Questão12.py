#Faça um programa que, dado um conjunto de N números, determine o menor
#valor, o maior valor e a soma dos valores.


n = int(input("Digite um número: "))
soma = 0
menor = n
maior = n
for i in range(1, n):
    n = int(input("Digite um número:"))
    soma = soma + n
    if n < menor:
        menor = n
        if n > maior:
            maior = n     
        else:
            print(f"O menor número é: {menor}")
            print(f"O maior número é: {maior}")
            print(f"A soma dos números é: {soma}")




