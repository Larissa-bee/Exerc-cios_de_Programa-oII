#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome= input("Digite seu nome:")
idade= input("Digite sua idade:") 
salario= input("Digite seu salário:")
sexo= input("Digite seu sexo (f ou m):")
estadocivil= input("Digite seu estado civil (s, c, v, ou d):")
if len(nome) >=3 and len(idade) >=0 or 150 and len(salario) <0 and sexo == 'f'and sexo == 'm' and estadocivil== 's' and estadocivil=='c' and estadocivil== 'v' and estadocivil== 'd': 
    print("Válido")
else:
    print("Inválido")
