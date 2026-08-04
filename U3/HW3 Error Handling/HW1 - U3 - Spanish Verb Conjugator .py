#This is a program about a conjugate regular spanish verb in present tense
Pronombres = ("Yo","Tu","El","Nosostros","Ellos","Ustedes")
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}
verb= input("Ingrese un verbo en infinitivo: ") #Este es el input, donde el usuario ingresa el verbo a modificar
stem= verb[:-2] #localiza la raiz del verbo 
end= verb[-2:] #localiza la terminacion del verbo
search= terminaciones[end] #Busca como termina el verbo
for i in range(len(Pronombres)): #usa el bucle for para ir modificando el verbo 
    print(Pronombres[i]+" "+ stem + search[i])
