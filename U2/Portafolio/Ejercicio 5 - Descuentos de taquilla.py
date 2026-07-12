#children  year > 12 = 30%
#students 12< year > 25 = 20%
#adults  26-65 = no discount
#oldman  year > 60 = 40%
price= 150
age= int(input("Ingresa la edad: "))
Card= input("Tienes tarjeta?(Si/No): ").lower()
if age <12:
    rate= price-.30*price
elif age <=25 and Card =="si":
    rate= price-.20*price
elif age <=65:
    rate= price
else:
    rate=price-.40*price
print (f"Price: {rate}")
    
