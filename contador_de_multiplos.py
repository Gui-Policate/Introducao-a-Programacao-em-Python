print("\n")
print("Olá, esse é um contador de multiplos")
print("Seu objetivo é verificar quanto multiplos um numero tem \n")
numero = float(input("Por favor informe o numero que deseja consultar: "))
contador = 1
multiplo = 0
while contador <= numero:
    resto = numero % contador 
    contador = contador + 1
    if resto == 0: 
        multiplo = multiplo + 1
print("O numero",numero ,"tem",multiplo ,"multiplos.")