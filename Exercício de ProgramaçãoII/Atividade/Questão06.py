'''Faça um programa que converta da notação de 24 horas para a notação de 12
horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para personalizar a saída.
'''

def converter_hr(h, m):
    if h == 0:
        return f'{h+12}:{m:02d} A.M.'
    elif h == 12:
        return f'{h}:{m:02d} P.M.'
    elif h > 12:
        return f'{h-12}:{m:02d} P.M.'
    else:
        return f'{h}:{m:02d} A.M.'
def saida():
    h= int(input("Digite a hora: "))
    m= int(input("Digite os minutos: "))
    print(converter_hr(h, m))
saida()

    