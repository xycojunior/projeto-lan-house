"""
O que o sistema deve fazer:
○ Nossa lan House possui 5 computadores disponíveis
■ O computador deve possuir: Identificador, Nome do locador, tempo( em horas)
locados
■ Determine o valor da hora da lan house (computadores tem o mesmo valor)
○ Reservar um computador (Check-in)
■ Caso não tenha mais nenhuma carro disponível, deverá informar ao usuário
■ Para fazer a reserva, apresente todos os computadores.
○ Saida (Check-out)
■ No check-out deverá se informado o computador que será fechado, e então
calcular o valor da fatura que deverá ser pago, com base nas horas
"""
#Criando variaveis para os ID´s dos computadores
idComputador1 = 1
idComputador2 = 2
idComputador3 = 3
idComputador4 = 4
idComputador5 = 5

#Criando variaveis para saber se os computadores estão ocupados
ocupado1 = "Não"
ocupado2 = "Não"
ocupado3 = "Não"
ocupado4 = "Não"
ocupado5 = "Não"

#declarando valor da hora
valorHora = 10
#
def menu():
    print("Bem-vindo a nossa Lan House, (valor da hora: R$10.00)")
    print("Escolha o dígito de um computador disponível abaixo: ")
    print("1 - Computador1")
    print("2 - Computador2")
    print("3 - Computador3")
    print("4 - Computador4")
    print("5 - Computador5")
    print("6 - Sair e fazer check-out\n")
    opcao = int(input("Escolha uma opção: "))
    return opcao

#repetição do menu de opções
while True:
    opcao = menu()

    #Criando a verificação pra saber se o computador está ocupado ou não, se não estiver faz o login.
    #
    print("\n")
    if opcao == 1:
        if ocupado1 == "Não":
            print("Você fez login no Computador 1")
            ocupado1 = "Sim"
        elif ocupado1 == "Sim":
            print("Computador Ocupado")
    #
    elif opcao == 2:
        if ocupado2 == "Não":
            print("Você fez login no Computador 2")
            ocupado2 = "Sim"
        elif ocupado2 == "Sim":
            print("Computador Ocupado")
    #
    elif opcao == 3:
        if ocupado3 == "Não":
            print("Você fez login no Computador 3")
            ocupado3 = "Sim"
        elif ocupado3 == "Sim":
            print("Computador Ocupado")
    #
    elif opcao == 4:
        if ocupado4 == "Não":
            print("Você fez login no Computador 4")
            ocupado4 = "Sim"
        elif ocupado4 == "Sim":
            print("Computador Ocupado")
    #
    elif opcao == 5:
        if ocupado5 == "Não":
            print("Você fez login no Computador 5")
            ocupado5 = "Sim"
        elif ocupado5 == "Sim":
            print("Computador Ocupado")
    
    elif opcao == 6:
        computador = int(input("Digite o computador que você deseja fazer Logout: "))
        if computador == 1:
            if ocupado1 == "Sim":
                horas = int(input("Quantas horas você passou? "))
                ocupado1 = "Não"
                print("Computador 1 fez logout!\n")
                print("Valor a ser pago é: R${}.00".format(valorHora * horas))

                if computador == 2:
                    if ocupado2 == "Sim":
                        horas = int(input("Quantas horas você passou? "))
                        ocupado2 = "Não"
                        print("Computador 2 fez logout!\n")
                        print("Valor a ser pago é: R${}.00".format(valorHora * horas))

                if computador == 3:
                    if ocupado3 == "Sim":
                        horas = int(input("Quantas horas você passou? "))
                        ocupado3 = "Não"
                        print("Computador 3 fez logout!\n")
                        print("Valor a ser pago é: R${}.00".format(valorHora * horas))

                if computador == 4:
                    if ocupado4 == "Sim":
                        horas = int(input("Quantas horas você passou? "))
                        ocupado4 = "Não"
                        print("Computador 4 fez logout!\n")
                        print("Valor a ser pago é: R${}.00".format(valorHora * horas))

                if computador == 5:
                    if ocupado5 == "Sim":
                        horas = int(input("Quantas horas você passou? "))
                        ocupado5 = "Não"
                        print("Computador 5 fez logout!\n")
                        print("Valor a ser pago é: R${}.00".format(valorHora * horas))
    print("\n")