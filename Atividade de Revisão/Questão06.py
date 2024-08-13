#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da
#pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
#deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
#"Assassino". Caso contrário, ele será classificado como "Inocente".


resp=0
resposta= input("Telefonou para a vítima? (S/N): ")
if resposta == "S" or resposta == "s":
    resp=resp+1
    resposta= input("Esteve no local do crime? (S/N): ")
    if resposta == "S" or resposta == "s":
        resp=resp+1
        resposta= input("Mora perto da vítima? (S/N): ")
        if resposta == "S" or resposta == "s":
            resp=resp+1
            resposta= input("Devia para a vítima? (S/N): ")
            if resposta == "S" or resposta == "s":
                resp=resp+1
                resposta= input("Já trabalhou com a vítima? (S/N): ")
                if resposta == "S" or resposta == "s":
                    resp=resp+1
                    print("A sua classificação é:")
                    if resp == 2:
                        print("Suspeito(a)")
                    elif resp == 3 or resp == 4:
                        print("Cúmplice")
                    elif resp == 5:
                        print("Assassino(a)")
                    else:
                        print("Inocente")





