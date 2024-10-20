resposta = "S"
while resposta == "S":
    print ("Olá essa é uma calculadora de Tabuadas!")
    while True:
        try:
            numero1 = float(input("A tabuada de qual numero deseja saber?: "))
            print ("Você deseja calcular a tabuada do número", numero1, "\n")
            break
        except:
            print ("Entrada Inválida!!!")
    while True:
        try:
            contador = float(input("A partir de quantas vezes deseja calcular?: "))
            print ("Sua tabuada ira iniciar o calculo a partir de", numero1, "x", contador, "\n")
            break
        except:
            print ("Entrada Inválida!!!")
    while True:
        try:
            numero2 = float(input("Até quantas vezes deseja calcular?: "))
            print ("Sua tabuada sera calculada até", numero1, "x", numero2, "\n")
            break
        except:
            print ("Entrada Invalida!!!")
    resposta = str(input("\nOs dados estão corretos, S/N?: ")).upper()
    respostas_possiveis = ["S", "N"]
    while resposta not in respostas_possiveis:
        resposta = str(input("Resposta Inválida!!!: ")).upper()
    print("\n")
    if resposta == "S":
        numero3 = numero2 + contador
        while contador <= numero3:
            numero = numero1 * contador
            print (numero1, "x", contador, "=", numero)
            contador = contador + 1
    resposta = str(input("\nDeseja realizar uma nova conta, S/N?: ")).upper()
    while resposta not in respostas_possiveis:
        resposta = str(input("Resposta Inválida: ")).upper()         
print("\nObrigado!!!\n")
