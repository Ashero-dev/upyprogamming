#Problema 4
end = "exit"
val = ""

# Listas de las estaciones
wntr = [12, 1, 2]
sprg = [3, 4, 5]
smmr = [6, 7, 8]
fall = [9, 10, 11]

while val != end: # Es el inicio de la condicion para tener los datos sobre meses
    val = input("Enter month or 'exit': ")
    
    if val.lower() == "exit": # Aqui el ciclo termina si el usuario usa 'exit'
        break
        
    if val != end:
        num = int(val) # Ingresa el mes en un numero
        
        # Aqui arroja los resultados de las estaciones
        if num in wntr:
            print("Winter")
        elif num in sprg:
            print("Spring")
        elif num in smmr:
            print("Summer")
        elif num in fall:
            print("Fall")
        else:
            print("Invalid month")
            print("Please enter a number between 1 and 12.")