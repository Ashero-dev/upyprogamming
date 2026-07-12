#imc 
#imc <18.5 = desnutrido
#imc <25 = normal
#imc 30 gotdito
#imc >=30 Majin boo
weigth= float(input("ingresa tu peso: "))
heigth= float(input("Ingrese su altura(m): "))
imc= weigth/(heigth*heigth)
if imc <18.5:
    print("Esta desnutrido")
elif imc <25:
    print("Estas normal")
elif imc <30:
    print("estas gordito")
else:
    print("Estas majin boo")
    