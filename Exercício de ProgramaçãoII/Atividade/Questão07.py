'''Crie uma função que receba um número indeterminado de valores inteiros e
depois apresente a soma deles na tela. Use: def nome_da_funcao (* parametro):'''

def soma(*valor):
    soma = 0
    for i in valor:
        soma += i
        return soma
print(soma(1, 2, 3, 4, 5, 6, 7))



    