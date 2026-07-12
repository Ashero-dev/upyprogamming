# Water Bill Calculator
end = "exit"
val = ""
total = 0

while val != end: # Es el inicio de la condicion para tener los datos
    val = input("Enter m3 or 'exit': ")
    
    if val.lower() == "exit": # Aqui el ciclo termina si el usuario usa 'exit'
        break
        
    if val != end:
        vol = float(val) # Ingresa el volumen en un numero float
        cost = 0
        
        # Aqui arroja los resultados dependiendo del consumo
        if vol <= 10:
            cost = vol * 8.00
            print(f"Month charge: ${cost:.2f}")
        elif vol <= 20:
            cost = vol * 12.00
            print(f"Month charge: ${cost:.2f}")
        else:
            cost = vol * 18.00
            print(f"Month charge: ${cost:.2f}")
            
        total = total + cost #suma acumulada de los meses

print(f"Total: ${total:.2f} ") #Promedio final y validacion