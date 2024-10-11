print("\n")
print("Olá, esse é um contador de múltiplos")
print("Seu objetivo é verificar quantos múltiplos um número tem \n")

resposta = "s"
while resposta == "S" or resposta == "s":
    numero = float(input("Por favor informe o número que deseja consultar: "))
    print ("O numero irformado é", numero,".")
    resposta = str(input("Esta correto, S(s) ou N(n)?"))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
    while resposta == "N" or resposta == "n":
        numero = float(input("Por favor informe o número que deseja consultar: "))
        print ("O numero irformado é", numero,)
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))

    print("\n")

    contador = 1
    multiplo = 0
    while contador <= numero:
        resto = numero % contador 
        contador = contador + 1
        if resto == 0: 
            multiplo = multiplo + 1
    print("O número",numero ,"tem",multiplo ,"múltiplos. \n")
    resposta = str (input("Deseja realizar uma nova consulta, S(s) ou N(n)?: "))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Deseja realizar uma nova consulta, S(s) ou N(n)?: "))
    
    print("\n")

print("Obrigado!!! \n")