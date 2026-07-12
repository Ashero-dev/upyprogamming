a= int(input("ingresa un numero para empezar un rango: "))
b= int(input("ingresa un numero para finalizar un rango: "))
for n in range (a,b+1):
    if n% 7 == 0:
        print("primer multiplo de 7: ",n)
        break
        
