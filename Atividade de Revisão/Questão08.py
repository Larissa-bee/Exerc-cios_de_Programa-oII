#Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
#Escreva um programa que pergunta a situação do usuário (se é idoso, se é
#gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
#prioridade ou não.

situacao= input("Digite sua situação (idoso, gestante ou PCD ou nenhum destes):")
if situacao == "idoso" or situacao == "idosa"  or situacao == "gestante" or situacao == "PCD":
    print("Você pode ter acesso a fila prioritária!")
else:
    print("Você não pode ter acesso!")