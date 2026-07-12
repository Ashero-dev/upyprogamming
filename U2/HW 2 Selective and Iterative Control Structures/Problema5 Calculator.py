# Prblema5 Calculator
end = "exit"
val = ""
total = 0

while val != end: # Es el inicio de la condicion para los envios
    val = input("Enter weight (kg) or 'exit': ")
    
    if val.lower() == "exit": # Aqui el ciclo termina si el usuario usa 'exit'
        break
        
    if val != end:
        weight = float(val) # Ingresa el peso en float
        dist = float(input("Enter distance (km): ")) # Ingresa la distancia
        cost = 0
        
        # Aqui arroja los resultados dependiendo de la distancia y peso
        if dist <= 100:
            if weight <= 5:
                cost = 50.00
            else:
                cost = 80.00
        else:
            if weight <= 5:
                cost = 120.00
            else:
                cost = 200.00
                
        print(f"Shipping cost: ${cost:.2f}")
        total = total + cost # Suma acumulada de los envios
        
print(f"Total: ${total:.2f}") # Validacion final del costo