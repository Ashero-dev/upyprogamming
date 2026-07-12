#Problema 8:
  #"lee una temperatura en Celsius e imprime el estado fisico del agua:
     #temp <= 0           -> "Solido (hielo)"
     #0 < temp < 100      -> "Liquido (agua)"
     #temp >= 100         -> "Gaseoso (vapor)"
temp= int(input("Ingresa la temperatura en grados celsius: "))
if temp <=0:
    print("Esta en estado solido")
elif temp <100:
    print("Esta en estado liquiido")
else:
    print("Esta en estado gaseoso")