import random
resposta = "s"
while resposta == "s":

    jogadas_autorizadas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    escolhas_possiveis = ["1", "2"]

    print ("\nOlá, bem vindo ao jogo de Par ou Impar contra o PC!!!")

    escolha = (input("\nPor favor escolha, 1 (Par) ou 2 (Impar): "))
    print ("Você escolheu", escolha)
    while escolha not in escolhas_possiveis:
        escolha = (input("Por favor escolha, 1 (Par) ou 2 (Impar): "))
        print ("Você escolheu", escolha)

    jogadas = (input("\nPor favor escolha um numero de 1 a 10: "))
    print ("Você escolheu o numero", jogadas)
    while jogadas not in jogadas_autorizadas:
        jogadas = (input("Por favor escolha um numero de 1 a 10:" ))
        print ("Você escolheu o numero", jogadas)
    jogadas1 = int(jogadas)

    numero_aleatorio = random.randint(1, 10)
    numero_aleatorio1 = int(numero_aleatorio)
    print ("\nO computador escolheu o numero", numero_aleatorio1)

    resultado = jogadas1 + numero_aleatorio1
    print("\nA soma das escolhas é", resultado)

    check1 = resultado % 2

    if check1 == 0 and escolha == "1":
        print("\nO número",resultado , "é um número par. Parabéns você ganhou!!!")

    if check1 == 0 and escolha == "2":
        print("\nO número" ,resultado , "é um número par. Você perdeu!!!")

    if check1 != 0 and escolha == "1":
        print("\nO número" ,resultado , " é um número impar. Você perdeu!!!")

    if check1 != 0 and escolha == "2": 
        print("\nO número" ,resultado , "é um numero impar Parabèns você ganhou!!!")

    respostas_possiveis = ["s", "n"]
    resposta = str(input("\nVocê deseja jogar novamente, s/n:? ")).lower()
    while resposta not in respostas_possiveis:
        resposta = str(input("\nVocê deseja jogar novamente, s/n"))
    print("\nObrigado!!!")
   


