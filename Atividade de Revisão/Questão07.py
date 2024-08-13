#Para votar, você deve ter entre 18 anos e menos de 65 anos. Escreva um
#programa que pergunte sua idade e diga se você é obrigado a votar ou não.

idade= int(input("Digite sua idade:"))
if idade >=18 and idade <=65:
    print("Você é obrigado a votar!")
else:
    print("Você não é obrigado a votar!")