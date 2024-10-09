print("\n")
print("Olá! Seja bem vindo ao meu conversor de moedas! \n")
opcao = int(input("Para converter qualquer moeda para o Real digite 1 ou 2 para converter o Real em qualquer outra moeda: "))
if opcao == 1:
    moeda = str(input("Qual moeda deseja converter para Real? "))
    valor = float(input("Qual o valor da cotação? "))
    quantia = float(input("Qual a quantia deseja converter em Real? "))
    cotacao = valor * quantia
    print ("$",quantia , moeda, "a uma cotação de $",valor , moeda,"por Real equivale a R$",cotacao ,"Real")
else:
    quantia = float(input("Quantos Reais deseja converter? "))
    moeda = str(input("Para qual moeda deseja converter seus Reais? "))
    valor = float(input("Qual a valor da cotação? "))
    cotacao = quantia / valor
    print("$",quantia, "Reais convertido em ", moeda, "a uma cotação de $", valor, moeda, "por Real equivale a $", cotacao, moeda)
resposta = str(input("Seseja realisar uma nova conversão S(s) ou N(n)"))
while resposta == "S" or resposta == "s":
    opcao = int(input("Para converter qualquer moeda para o Real digite 1 ou 2 para converter o Real em qualquer outra moeda: "))
    if opcao == 1:
        moeda = str(input("Qual moeda deseja converter para real? "))
        valor = float(input("Qual o valor da cotação? "))
        quantia = float(input("Qual a quantia deseja converter em Real? "))
        cotacao = valor * quantia
        print ("$",quantia , moeda, "a uma cotação de $",valor , moeda," por Real equivale a R$",cotacao ,"Reais")
    else:
        quantia = float(input("Quantos Reais deseja converter? "))
        moeda = str(input("Para qual moeda deseja converter seus Reais? "))
        valor = float(input("Qual a valor da cotação? "))
        cotacao = quantia / valor
        print("$",quantia, "Reais convertido em ", moeda, "a uma cotação de $", valor, moeda, "por Real equivale a $", cotacao, moeda)
    resposta = str(input("Deseja realisar uma nova conversão S(s) ou N(n)"))
else:
    print("Obrigado pela preferência")