#suma pares
n=int(input("ingresa un numero: "))
res=0
for i in range (2,n+1,2):
    res=res+i
    print(i)
print("suma de pares", res)