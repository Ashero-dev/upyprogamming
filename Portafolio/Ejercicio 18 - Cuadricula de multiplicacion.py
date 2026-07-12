n=int(input("ingresa un numero: "))
for r in range (1,n+1):
    linea=""
    for c in range (1, n+1):
        linea=linea+ str(r*c) +  "\t"
        print(linea)
    