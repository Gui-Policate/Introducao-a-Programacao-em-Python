print("\n")
print("Olá, esse é um contador de múltiplos")
print("Seu objetivo é verificar quanto múltiplos um número tem \n")
numero = float(input("Por favor informe o número que deseja consultar: "))
contador = 1
multiplo = 0
while contador <= numero:
    resto = numero % contador 
    contador = contador + 1
    if resto == 0: 
        multiplo = multiplo + 1
print("O número",numero ,"tem",multiplo ,"múltiplos.")