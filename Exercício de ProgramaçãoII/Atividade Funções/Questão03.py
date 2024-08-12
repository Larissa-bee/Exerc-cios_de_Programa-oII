'''Faça um programa que receba três números do usuário, e identifique o maior
através de uma função e o menor número através de outra função.
'''

num1= int(input("Digite um número: "))
num2= int(input("Digite outro número: "))
num3= int(input("Digite mais um número: "))
def maior(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
def menor(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3
print("O maior número é: ", maior(num1, num2, num3))
print("O menor número é: ", menor(num1, num2, num3))


#ou


def maior(num1, num2, num3):
    maior= max(num1, num2, num3)
    return maior
def menor(num1, num2, num3):
    menor= min(num1, num2, num3)
    return menor
num1= int(input("Digite um número: "))
num2= int(input("Digite outro número: "))
num3= int(input("Digite mais um número: "))
print(f"O maior número é :{maior(num1, num2, num3)}\n E o menor {menor(num1, num2, num3)}")