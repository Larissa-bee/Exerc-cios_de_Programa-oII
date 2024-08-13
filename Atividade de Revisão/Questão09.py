#Faça um programa que leia um nome de usuário e a sua senha e não aceite
#a senha igual ao nome do usuário, mostrando uma mensagem de erro e
#voltando a pedir as informações.

nome= input("Digite seu nome:")
senha= input("Digite sua senha:")

while nome == senha:
    print("ERRO, NOME E SENHA IGUAIS!")
    nome= input("Digite seu nome:")
    senha= input("Digite sua senha:")

print("Cadastro feito com sucesso!")

