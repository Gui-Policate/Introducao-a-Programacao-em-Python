print("\n")
print("Olá esse e um pequeno software capaz de realizar contagen de números inteiros \n")

resposta = "s"
while resposta == "S" or resposta == "s":
    inicio = int(input("Por favor informe o numero de inicio da contagem: "))
    print ("Você deseja iniciar a contagem a partir no numero", inicio)
    resposta = str(input("Esta correto, S(s) ou N(n)? "))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Esta correto, S(s) ou N(n)? "))
        while resposta == "N" or resposta == "n":
            inicio = int(input("por favor informe o numero de inicio da contagem "))
            print ("Você deseja iniciar a contagem a partir no numero", inicio)
            resposta = str(input("Esta correto, S(s) ou N(n)? "))
    
    print ("\n")

    numerica = int(input("Por favor digite o tamanho da sequência desejada: "))
    print("A sequência numérica desejada é de", numerica, "algarismos")
    resposta = str(input("Esta correto, S(s) or N(n)? "))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Esta correto, S(s) ou N(n)? "))
        while resposta == "N" or resposta == "n":
            numerica = int(input("Por favor digite o tamanho da sequência desejada: "))
            print("A sequência numérica desejada é de", numerica, "algarismos")
            resposta = str(input("Esta correto, S(s) or N(n)? "))
            
    contador = 0
    while(contador < numerica):
        contador = contador + 1 
        inicio = inicio + 1
        print(inicio)
    
    resposta = str(input("Deseja realizar nova consulta, S(s) ou N(n)?: "))
    while (resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n"):
        resposta = str(input("Deseja realizar nova consulta, S(s) ou N(n)?: "))
    
print("\n")
print("Obrigado!!!")