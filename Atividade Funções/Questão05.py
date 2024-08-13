'''Escreva um programa que possa cadastrar clientes ou funcionários para uma
loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
Utilize comandos de manipulação de string para personalizar a saída.'''


def cadas_cliente():
    nome = input("Digite o nome do cliente:")
    endereco = input("Digite o endereço do cliente:")
    cpf = input("Digite o CPF do cliente:")
    print(f"Nome: {nome}\n Endereço: {endereco}\n CPF: {cpf}")
    return nome, endereco, cpf
def cadas_funcionario():
    nome = input("Digite o nome do funcionário: ")
    salario = input("Digite o salário do funcionário:")
    cargo = input("Digite o cargo do funcionário:")
    cpf = input("Digite o CPF do funcionário:")
    print(f"Nome: {nome}\n Salário: {salario}\n Cargo: {cargo}\n CPF: {cpf}")
    return nome, salario, cargo, cpf
def main():
    while True:
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar funcionário")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cadas_cliente()
        elif escolha == "2":
            cadas_funcionario()
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")
main()
