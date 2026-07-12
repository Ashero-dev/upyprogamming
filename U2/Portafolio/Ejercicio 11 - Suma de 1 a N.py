
#Problema 11:
 # Lee un entero positivo N e imprime la suma 1 + 2 + ... + N usando un
 # ciclo while (inicializa, condicion, actualiza).
num=int(input("Ingresa cuantas numeros deseas sumar: "))
contador=0
suma=0
while contador<num:
    nume= int(input("Ingresa el numero: "))
    suma= nume + suma
    contador+=1
    print(nume)
print (f"suma:  {suma}")
    

