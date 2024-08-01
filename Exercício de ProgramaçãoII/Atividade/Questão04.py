'''Crie um programa de câmbio. Nesse programa adicione funções que
realizem conversões de real para dólar, real para euro e real para peso
argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
1,00 real = 0,18 dólar para Estados Unidos;
1,00 real = 0,16 euro para Portugal;
1,00 real = 0,0061 peso para Argentina;
'''


def real_dolar(real, dolar):
    return real * dolar

def real_euro(real, euro):
    return real * euro

def real_peso(real, peso):
    return real * peso

def main():

    real= 1.00
    dolar = 0.18
    euro = 0.16
    peso = 165

    valor = float(input("Digite o valor (em real): "))
    pais = input("Digite o país (Estados Unidos, Portugal ou Argentina): ")
    if pais == "Estados Unidos":
        print(f"{valor} equivale a: ", real_dolar(real, dolar))
    elif pais == "Portugal":
        print(f"{valor} equivale a: ", real_euro(real, euro))
    elif pais == "Argentina":
        print(f"{valor} equivale a: ", real_peso(real, peso))
    else:
        print("País não encontrado")

main()

    
