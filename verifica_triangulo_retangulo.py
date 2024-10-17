import math
resposta = "s"
while resposta == "S" or resposta == "s":
    print("Olá, essa é uma calculadora de Triângulo Retângulo da medida dos lados!")
    print("Digite 1 caso queria saber se as 3 medida correspondem a um Triângulo Retângulo!")
    print("Digite 2 caso queira saber a medida do Cateto que esta faltando!")
    print("Digite 3 caso queira saber a medida da Hipotenusa!")
    opcao = input("Opção: ")
    while (opcao != "1" and opcao != "2" and opcao != "3"):
       opcao = input("Por favor escolha uma das opções sugeridas!")
    print("\n")
    if opcao == "1":
        print("Você escolheu a opção 1!")
        while True:
            try:
                cateto1 = float(input("Por favor informe a medida do primeiro Cateto: "))
                break
            except: 
                print("Entrada Invalida. Por favor digite somente os numeros da medida solicitada!")
        while True:    
            try:
                cateto2 = float(input("Por favor informe a meedidao do segundo Cateto: "))
                break
            except: 
                print("Entrada Invalida. Por favor digite somente os numeros da medida solicitada!")
        while True:    
            try:     
                hipotenusa = float(input("Por favor informe a medida da Hipotenusa: "))
                break
            except: 
                print("Entrada Invalida. Por favor digite somente os numeros da medida solicitada!")
        medida1 = (cateto1 * cateto1) + (cateto2 * cateto2)
        medida2 = (hipotenusa * hipotenusa)
        if medida1 == medida2:
            print("Essas medidas correspondem a um Triângulo Retângulo! \n")
        else:
            print("Essas medidas não correspondem a um Triângulo Retângulo! \n")
   
    if opcao == "2":
        print("Você escolheu a opção 2!")
        while True:
            try:
                cateto1 = float(input("Por favor informe a medida do Cateto: "))
                break
            except: 
                print("Entrada Invalida. Por favor digite somente os numeros da medida solicitada!")
        while True:    
            try:     
                hipotenusa = float(input("Por favor informe a medida da Hipotenusa: "))
                break
            except: 
                print("Entrada Invalida. Por favor digite somente os numeros da medida solicitada!")
        medida1 = (hipotenusa * hipotenusa) - (cateto1 * cateto1)
        cateto2 = math.sqrt(medida1)
        print("A medida do Cateto que esta faltando para formar um Triângulo Retângulo é ",cateto2 ,"\n")
    
    if opcao == "3":
        print("Você escolheu a opção 3!")
        while True:
            try:
                cateto1 = float(input("Por favor informe a medida do primeiro Cateto: "))
                break
            except: 
                print("Entrada Invalida. Por favor digite somente os numeros da medida solicitada!")
        while True:    
            try:     
                cateto2 = float(input("Por favor informe a medida so segundo Cateto: "))
                break
            except: 
                print("Entrada Invalida. Por favor digite somente os numeros da medida solicitada!")
        medida1 = (cateto2 * cateto2) + (cateto1 * cateto1)
        hipotenusa = math.sqrt(medida1)
        print("A medida que esta faltando refente a Hipotenusa para formar um Triângulo Retângulo é ",hipotenusa ,"\n")

    resposta = input("Deseja realizar uma nova consulta S(s) ou N(n)?: ")
    while resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n":
        resposta = input("Por favor escolha uma das opções acima!")
print("Obrigado!")
