resposta = "s"
while resposta == "s":
    print ("\nOlá, essa é uma espécie de claculadora que irá te ajudar com números primos!")

    print ("\nPor favor informe qual a opção desejada;")
    print ("1 = Para verificar se um número é ou não primo;")
    print ("2 = Para saber quais são os números primos em um determinado intervalo:")
    opcoes_obrigatorias = ["1", "2"]
    opcao = str(input("1 ou 2?: "))
    while opcao not in opcoes_obrigatorias:
        print ("1 ou 2?: ")

    if opcao == "1":
        contador = 1 
        resto = 1 
        resultado = 0
        # Bloquei para usuário digitar apenas número inteiros
        while True:
            try:
                numero1 = int(input("\nQual número deseja verificar?: "))
                break
            except:
                numero1 = int(input("\nQual número deseja verificar?: "))
        # Loop de teste para verificação do numero desejado pelo usuário
        while contador <= numero1:
            if numero1 % contador == 0:
                resto = resto + 1
            contador = contador + 1
        if resto != 2:
            print("O número", numero1, "não é um número primo!!!")
        else:
            print("O número", numero1, "é um número primo!!!")

    # A idéia aqui é que a calculadora informe quais são os numeros primos dentro do intervalo apresentado pelo usuário
    if opcao == "2":
        # Bloquei para usuário digitar apenas número inteiros
        while True:
            try:
                inicio = int(input("\nInforme um número inicial para o intervalo diferente de 0.: "))
                # Bloqueio para que o usuário não possa tentar uma divisão por zero
                if inicio != 0:
                    break
            except:
                inicio = int(input("\nInforme um número inicial para o intervalo diferente de 0.: "))
        # Bloqueio para usuário digitar apenas numerios inteiros
        while True:
            try:
                final = int(input("\nInforme um número final para o intervalo maior ou igual ao inicial.: "))
                # Bloqueio para o usuario digitar um número maior ou igual que o anterior
                if final >= inicio: 
                    break
            except:
                final = int(input("\nInforme um número final para o intervalo maior ou igual ao inicial.: "))
        # As variaveis contador e resultado são zeradas dentro do lood do intervalo         
        while inicio <= final:
            contador = 1
            resultado = 0
            # Aqui Ocorre a verificação se o número é primo ou não do início até o final
            while contador <= inicio:
                if inicio % contador == 0:
                    resultado = resultado + 1
                contador = contador + 1  
            if resultado == 2: 
                print ("-->", inicio)
            inicio = inicio + 1
    
    # Estrutura de repetição ou encerramento do código
    respostas_possiveis = ["s", "n"]        
    resposta = str(input("Deseja realizar uma nova consulta; s/n?: ")).lower()
    while resposta not in respostas_possiveis:
        resposta = str(input("Deseja realizar uma nova consulta; s/n?: ")).lower()
print ("Obrigado!!!")
