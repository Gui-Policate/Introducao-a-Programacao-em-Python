print("\n")
print("Olá, bem vindo \n")
print("Essa é um calculadora verificadora de números múltiplos entre si")
resposta = "s"
while resposta == "S" or resposta == "s":
    num1 = float(input("Por favor digite o primeiro número desejado: "))
    print ("Você digitou o número", num1)
    resposta = str(input("Esta correto, S(s) ou N(n)?: "))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
    while resposta == "N" or resposta == "n":
        num1 = float(input("Por favor digite o primeiro numero desejado: "))
        print ("Você digitou o número ", num1)
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))  

    print("\n") 

    num2 = float(input("Por favor digite o segundo numento desejado que deve ser diferente se 0: "))
    print ("Você digitou o número ", num2)
    while num2 == 0:
        num2 = float(input("Por favor digite um segundo numero diferente de 0: "))
        print ("Você digitou o número ", num2)
    resposta = str(input("Esta correto, S(s) ou N(n)?: "))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
    while resposta == "N" or resposta == "n":
        num2 = float(input("Por favor digite o segundo numento desejado que deve ser diferente de 0: "))
        while num2 == 0:
            num2 = float(input("Por favor digite um segundo numero diferente de 0: "))
        print ("Você digitou o número ", num2, ". \n")
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))
       
    resto = (num1 % num2)
    if resto == 0:
        print("O", num1, "é múltiplo do ", num2, ". \n")
    else:
        print("O", num1, "não é múltiplo do número ", num2, ". \n")

    resposta = str(input("Deseja realizar uma nova consulta, S(s) ou N(n)?: "))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Deseja realizar uma nova consulta S(s) ou N(n)?: "))
print("Obrigado!!! \n")
    