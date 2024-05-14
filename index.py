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
#Criando variaveis para saber se os computadores estão ocupados
ocupado1 = "Não"
ocupado2 = "Não"
ocupado3 = "Não"
ocupado4 = "Não"
ocupado5 = "Não"
#Criando variaveis para guardar os nomes dos usuarios
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
    print("Escolha um computador disponível abaixo para fazer login: ")
    print("0 - Ver computadores em uso")
    print("1 - Computador1")
    print("2 - Computador2")
    print("3 - Computador3")
    print("4 - Computador4")
    print("5 - Computador5")
    print("6 - Sair e fazer check-out")
    print("7 - encerrar aplicação\n")
    opcao = int(input("Escolha uma opção: "))
    return opcao

#repetição do menu de opções, loop principal do codigo:
while True:
    opcao = menu()
    #verificação e listagem dos computadores em uso com seus respectivos usuarios
    if opcao == 0:
        print("\nComputadores em uso: ")
        if ocupado1 == "Sim":
            print("Computador 1 está ocupado por:",usuario1)
        if ocupado2 == "Sim":
            print("Computador 2 está ocupado por:",usuario2)
        if ocupado3 == "Sim":
            print("Computador 3 está ocupado por:",usuario3)
        if ocupado4 == "Sim":
            print("Computador 4 está ocupado por:",usuario4)
        if ocupado5 == "Sim":
            print("Computador 5 está ocupado por:",usuario5)
        else:
            print("Todos os computadores estão livres")

    #realizando login nos computadores e atribuindo usuarios a eles           
    if opcao == 1:
        if ocupado1 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario1 = dadosUser
            print("Bem-vindo",usuario1,"você fez login no Computador 1")
            ocupado1 = "Sim"
        else:
            print("Computador ocupado por",usuario1,"escolha outro!\n") 

    elif opcao == 2:
        if ocupado2 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario2 = dadosUser
            print("Bem-vindo",usuario2,"você fez login no Computador 2")
            ocupado2 = "Sim"
        else:
            print("Computador ocupado por",usuario2,"escolha outro!\n") 

    elif opcao == 3:
        if ocupado3 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario3 = dadosUser
            print("Bem-vindo",usuario3,"você fez login no Computador 3")
            ocupado3 = "Sim"
        else:
            print("Computador ocupado por",usuario3,"escolha outro!\n") 

    elif opcao == 4:
        if ocupado4 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario4 = dadosUser
            print("Bem-vindo",usuario4,"você fez login no Computador 4")
            ocupado4 = "Sim"
        else:
            print("Computador ocupado por",usuario4,"escolha outro!\n") 

    elif opcao == 5:
        if ocupado5 == "Não":
            dadosUser = input("Digite seu nome: ")
            usuario5 = dadosUser
            print("Bem-vindo",usuario5,"você fez login no Computador 5")
            ocupado5 = "Sim"
        else:
            print("Computador ocupado por",usuario5,"escolha outro!\n") 
    
    #realizando o logout dos computadores 
    elif opcao == 6:
        dadosUser = input("Digite seu nome para fazer logout: ")
        computador = int(input("Digite o computador que você deseja fazer Logout: "))
#computador1  
        if computador == 1:
            if ocupado1 == "Sim":
                if usuario1 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado1 = "Não"
                    print("\nComputador 1 irá ser fechado e fazer logout!")
                    print(usuario1, "você passou",horas, "hora(s) logado, seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!") 
            else:
                print("Computador 1 não está ocupado.\n")
#computador2             
        elif computador == 2:
            if ocupado2 == "Sim":
                if usuario2 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado2 = "Não"
                    print("\nComputador 2 irá ser fechado e fazer logout!")
                    print(usuario2, "você passou",horas, "hora(s) logado, seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
            else:
                print("Computador 2 não está ocupado.\n")
#computador3  
        elif computador == 3:
            if ocupado3 == "Sim":
                if usuario3 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado3 = "Não"
                    print("\nComputador 3 irá ser fechado e fazer logout!")
                    print(usuario3, "você passou",horas, "hora(s) logado, seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
            else:
                print("Computador 3 não está ocupado.\n")
#computador4
        elif computador == 4:
            if ocupado4 == "Sim":
                if usuario4 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado4 = "Não"
                    print("\nComputador 4 irá ser fechado e fazer logout!")
                    print(usuario4, "você passou",horas, "hora(s) logado, seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
            else:
                print("Computador 4 não está ocupado.\n")
#computador5  
        elif computador == 5:
            if ocupado5 == "Sim":
                if usuario5 == dadosUser:
                    horas = int(input("Quantas horas você passou? "))
                    ocupado5 = "Não"
                    print("\nComputador 5 irá ser fechado e fazer logout!")
                    print(usuario5, "você passou",horas, "hora(s) logado, seu valor a ser pago é: R${}.00".format(valorHora * horas))
                    print("Obrigado e volte sempre!")
            else:
                print("Computador 5 não está ocupado.\n")
    elif opcao == 7:
        print("Você encerrou a aplicação!")
        break
        
#Verificação para saber se o usuario informou um valor não definido:
    elif opcao >= 8: 
        print("opção inválida, digite um valor de 0 a 7")