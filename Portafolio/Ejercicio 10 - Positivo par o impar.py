#Problema 10:
 # Lee un numero. Si es positivo, indica si es "Positivo par" o
 # "Positivo impar". Si no es positivo, imprime "No es positivo".
num= int(input("Ingresa un numero: "))
if num >=0:
    if num % 2==0:
        print("es un numero positivo par")
    else:
        print("Es un positivo impar")
else:
    print("No es positivo")