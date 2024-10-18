resposta = "s"
while resposta == "S" or resposta == "s":
    import math
    print ("Olá, essa e uma calculadora de círculos.")
    print ("1 = Calcular o Raio com a medida do Diâmetro.")
    print ("2 = Calcular o Raio com a medida da Circunferência.")
    print ("3 = Calcular o Raio com a medida da Área.")
    print ("4 = Calcular o Diâmetro com a medida do Raio.")
    print ("5 = Calcular o Diâmetro com a medida da Circunferência.")
    print ("6 = Calcular o Diâmetro com a medida da Área.")
    print ("7 = Calcular a Circunferência com a medida do Raio.")
    print ("8 = Calcular a Circunferência com a medida do Diâmetro")
    print ("9 = Calcular a Circunferência com a medida da Área")
    print ("10 = Calcular a Área com a medida do Raio.")
    print ("11 = Calcular a Área com a medida do Diâmetro")
    print ("12 = Calcular a Área com a medida da Circunferência")
    opcoes_validas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    opcao = input ("Escolha uma opção: ")
    while opcao not in opcoes_validas:
        opcao = input ("escolha uma opção valida: ")
    print("\n")
    print ("Você escolheu a opcao", opcao)
    if opcao == "1":
        while True:
            try:
                diametro = float(input("Informe a medida do Diâmetro: "))
                raio = diametro / 2
                print ("O Raio mede", raio)
                break
            except:
                print("Entrada inválida.")
    if opcao == "2":
        while True:
            try:
                circunferencia = float(input("informe a medida da Circunerência: "))
                raio = circunferencia / (2 * math.pi)
                print ("O Raio mede", raio)
                break
            except:
                print ("Entrada inválida.")
    if opcao == "3":
        while True:
            try:
                area = float(input("Informe a medida da Área: "))
                raio = math.sqrt(area * math.pi)
                print ("O Raio mede", raio)
                break
            except:
                print ("Entrada inválida")
    if opcao == "4":
        while True:
            try:
                raio = float(input("Informe a medida do Raio: "))
                diametro = raio * 2
                print ("O Diâmetro mede", diametro)
                break
            except:
                print ("Entrada inválida")
    if opcao == "5":
        while True:
            try:
                circunferencia = float(input("Informa a medida da Circunferência: "))
                diametro = circunferencia / math.pi
                print (" O Diâmetro mede", diametro)
                break
            except:
                print ("Entrada inválida")
    if opcao == "6":
        while True:
            try:
                area = float(input("Informe a medida da Área: "))
                diametro = 2 * (math.sqrt(area / math.pi))
                print ("O Diâmentro", diametro)
                break
            except:
                print ("Entrada inválida")
    if opcao == "7":
        while True:
            try:
                raio = float(input("Informe a medida do Raio: "))
                circunferencia = 2 * math.pi * raio
                print ("A Circunferência mede", circunferencia)
                break
            except:
                print ("Entrada inválida")
    if opcao == "8":
        while True:
            try:
                diametro = float(input("Informe a medida do Diâmetro: "))
                circunferencia = 2 * math.pi * (diametro / 2)
                print ("A Circunferência mede", circunferencia)
                break
            except:
                print ("Entrada inválida")
    if opcao == "9":
        while True:
            try:
                area = float(input("Informe a medida da Área: "))
                circunferencia = 2 * math.sqrt(math.pi * area)
                print ("A Circunferência mede", circunferencia)
                break
            except:
                print ("Entrada inválida")
    if opcao == "10":
        while True:
            try:
                raio = float(input("Informe a medida do Raio: "))
                area = math.pi * raio ** 2
                print ("A Área mede", area)
                break
            except:
                print ("Entrada inválida")
    if opcao == "11":
        while True: 
            try:
                diametro = float(input("Informe a medida do Diâmetro: "))
                area = math.pi * ((diametro / 2) ** 2)
                print ("A Área mede", area)
                break
            except:
                print ("Entrada inválida")
    if opcao == "12":
        while True:
            try:
                circunferencia = float(input("Informe a medida da Circunferência: "))
                area = circunferencia ** 2 / ( 4 * math.pi)
                print ("A Área mede", area)
                break
            except:
                print("Entrada inválida")
    print ("\n")
    resposta = str(input("Deseja realizar outra operação, S(s) ou N(n)?: "))
    while resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n":
        resposta = str(input("Deseja realizar outra operação, S(s) ou N(n)?: "))
    print("\n")
print ("Obrigado!!!")