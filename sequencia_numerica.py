print("Olá esse e um pequeno software capaz de realizar contagen numericas \n")

print("\n")

inicio = int(input("por favor informe o numero de inicio da contagem \n"))
numerica = int(input("Por favor digite o tamanho da sequência desejada \n"))
contador = 0
while(contador < numerica):
    contador = contador +1 
    inicio = inicio + 1
    print(inicio)
pergunta = input("desja realizar nova consulta S(s) ou N(n)? \n")
while (pergunta == "S") or pergunta == "s":
    inicio = int(input("por favor informe o numero de inicio da contagem \n"))
    numerica = int(input("Por favor digite o tamanho da sequência desejada \n"))
    contador = 0
    while(contador < numerica):
        contador = contador +1 
        inicio = inicio + 1
        print(inicio)
    pergunta = input("desja realizar nova consulta S(s) ou N(n)? \n")
else:
    print("Obrigado!!! Volte Sempre!!!")