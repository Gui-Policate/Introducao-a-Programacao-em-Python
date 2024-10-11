print("\n")
print("Olá! Seja bem vindo ao meu conversor de moedas! \n")
resposta = "s"
while resposta == "S" or resposta == "s":
    opcao = int(input("Para converter qualquer moeda para o Real digite 1 ou 2 para converter o Real em qualquer outra moeda: "))
    print ("Você digitou a opção", opcao)
    resposta = str (input("Esta correto, S(s) ou N(n)?: "))
    while resposta == "N" or resposta == "n":
        opcao = int(input("Para converter qualquer moeda para o Real digite 1 ou 2 para converter o Real em qualquer outra moeda: "))
        print ("Você digitou a opção", opcao)
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
    if opcao == 1:
        print ('\n')
        moeda = str(input("Qual moeda deseja converter para Real?: "))
        print ("Você deseja converter", moeda, "para Real")
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while resposta == "N" or resposta == "n":
            moeda = str(input("Qual moeda deseja converter para Real?: "))
            print ("Você deseja converter", moeda, "para Real")
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        print("\n")
        valor = float(input("Qual o valor da cotação: "))
        print ("1", moeda, "esta valendo $",valor, "Reais")
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while resposta == "N" or resposta == "n":
            valor = str(input("Qual valor da cotação: "))
            print ("1", moeda, "esta valendo $",valor, "Reais")
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        print("\n")
        quantia = float(input("Qual a quantia deseja converter em Reais?: "))
        print ("Você deseja converter $",quantia,moeda, "em Reais")
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while resposta == "N" or resposta == "n":
            quantia = float(input("Qual a quantia deseja converter em Reais?: "))
            print ("Você deseja converter $",quantia,moeda, "em Reais")
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))

        print("\n")
        cotacao = valor * quantia
        print ("$",quantia , moeda, "a uma cotação de $",valor , moeda,"por Real equivale a R$",cotacao ,"Reais \n")
        
    else:
        print("\n")
        quantia = float(input("Quantos Reais deseja converter?: "))
        print("Você deseja converter $",quantia, "Reais em outra moeda")
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while resposta == "N" or resposta == "n":
            quantia = float(input("Quantos Reais deseja converter?: "))
            print("Você deseja converter $",quantia, "Reais em outra moeda")
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        print("\n")
        moeda = str(input("Para qual moeda deseja converter seus Reais?: "))
        print("Você deseja converter $",quantia, "Reais para", moeda, "?")
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while resposta == "N" or resposta == "n":
            moeda = str(input("Para qual moeda deseja converter seus Reais?: "))
            print("Você deseja converter $",quantia, "Reais para", moeda, "?")
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        print("\n")
        valor = float(input("Qual a valor da cotação: "))
        print ("1", moeda, "esta valendo $",valor,"Reais")
        resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        while resposta == "N" or resposta == "n":
            valor = float(input("Qual a valor da cotação: "))
            print ("1", moeda, "esta valendo $",valor,"Reais")
            resposta = str(input("Esta correto, S(s) ou N(n)?: "))
        print("\n")
        cotacao = quantia / valor
        print("$",quantia, "Reais convertido em", moeda, "a uma cotação de $", valor, moeda, "por Real equivale a $", cotacao, moeda, "\n")

    resposta = str(input("Deseja realisar uma nova conversão S(s) ou N(n) \n"))

print("Obrigado!!! \n")