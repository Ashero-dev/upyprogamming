#for palabra
palabra =input("ingresa una palabra: ")
contar=0
for i in palabra.lower():
    if i in "aeiou":
        contar = contar +1
print("contiene tantas vocales: ", contar)