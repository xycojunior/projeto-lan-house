"""
O que o sistema deve fazer:
○ Nossa lan House possui 5 computadores disponíveis
■ O computador deve possuir: Identificador, Nome do locador, tempo( em horas)
locados
■ Determine o valor da hora da lan house (computadores tem o mesmo valor)
○ Reservar um computador (Check-in)
■ Caso não tenha mais nenhuma computador disponível, deverá informar ao usuário
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

usuario1 = "Não"
usuario2 = "Não"
usuario3 = "Não"
usuario4 = "Não"
usuario5 = "Não"

#declarando valor da hora
valorHora = 10

#criando a função para rodar o menu
def menu():
    print("\nBem-vindo a nossa Lan House (valor da hora: R$10.00)")
    print("Escolha um computador disponível abaixo para logar: ")
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
    if opcao == 1:
        if ocupado1 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario1 = dadosUser
            print("Bem-vindo!", usuario1, "você fez login no Computador 1\n")
            ocupado1 = "Sim"
        else:
            print("Computador ocupado por", usuario1, "escolha outro!\n") 

    elif opcao == 2:
        if ocupado2 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario2 = dadosUser
            print("Bem-vindo!", usuario2, "você fez login no Computador 2\n")
            ocupado2 = "Sim"
        else:
            print("Computador ocupado por", usuario2, "escolha outro!\n") 

    elif opcao == 3:
        if ocupado3 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario3 = dadosUser
            print("Bem-vindo!", usuario3, "você fez login no Computador 3\n")
            ocupado3 = "Sim"
        else:
            print("Computador ocupado por", usuario3, "escolha outro!\n") 

    elif opcao == 4:
        if ocupado4 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario4 = dadosUser
            print("Bem-vindo!", usuario4, "você fez login no Computador 4\n")
            ocupado4 = "Sim"
        else:
            print("Computador ocupado por", usuario4, "escolha outro!\n") 

    elif opcao == 5:
        if ocupado5 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario5 = dadosUser
            print("Bem-vindo!", usuario5, "você fez login no Computador 5\n")
            ocupado5 = "Sim"
        else:
            print("Computador ocupado por", usuario5, "escolha outro!\n") 
    
    #realizando o logout dos computadores 
    if opcao == 6:
        computador = int(input("Digite o computador que você deseja fazer Logout: "))
        if computador == 1:
            if ocupado1 == "Sim":
                if usuario1 == dadosUser:  # Verifica se o usuário corresponde ao que está fazendo logout
                    horas = int(input("Quantas horas você passou? "))
                    ocupado1 = "Não"
                    print("Computador 1 fez logout!")
                    print(usuario1, "seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
                else:
                    print("Usuário incorreto para o Computador 1.\n")
            else:
                print("Computador 1 não está ocupado.\n")
        elif computador == 2:
            if ocupado2 == "Sim":
                if usuario2 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado2 = "Não"
                    print("Computador 2 fez logout!")
                    print(usuario2, "seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
                else:
                    print("Usuário incorreto para o Computador 2.\n")
            else:
                print("Computador 2 não está ocupado.\n")
        elif computador == 3:
            if ocupado3 == "Sim":
                if usuario3 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado3 = "Não"
                    print("Computador 3 fez logout!")
                    print(usuario3, "seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
                else:
                    print("Usuário incorreto para o Computador 3.\n")
            else:
                print("Computador 3 não está ocupado.\n")
        elif computador == 4:
            if ocupado4 == "Sim":
                if usuario4 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado4 = "Não"
                    print("Computador 4 fez logout!")
                    print(usuario4, "seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
                else:
                    print("Usuário incorreto para o Computador 4.\n")
            else:
                print("Computador 4 não está ocupado.\n")
        elif computador == 5:
            if ocupado5 == "Sim":
                if usuario5 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado5 = "Não"
                    print("Computador 5 fez logout!")
                    print(usuario5, "seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
                else:
                    print("Usuário incorreto para o Computador 5.")
            else:
                print("Computador 5 não está ocupado.\n")
