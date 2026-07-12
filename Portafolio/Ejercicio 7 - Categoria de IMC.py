#red = stop, yellow= warring green = go
# Any color = invalid
color= input("Ingresa un color: ").lower()
if color == "verde":
    print("go")
elif color == "amarillo":
    print("Warring")
elif color == "rojo":
    print("Stop")
else:
    print("Ingrese un color valido")