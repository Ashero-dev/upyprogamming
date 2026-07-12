end= "exit"
weight=""
while weight != end:
    weight= input("ingresa tu peso: ")
    if weight.lower()=="exit":
        break #Aqui el ciclo termina si el usuario usa "exit"
    if weight != end:
        height= float(input("Ingrese su altura(m): "))
        weightnum = int(weight)
        imc= weightnum/(height*height)

        if imc < 18.5:
            print(f"weight = {weightnum}, height = {height} BMI: {imc:.2f} — Underweight")
        elif imc <= 24.9:
            print(f"weight = {weightnum}, height = {height} BMI: {imc:.2f} — Normal")
        elif imc <= 29.9:
            print(f"weight = {weightnum}, height = {height} BMI: {imc:.2f} — Overweight")
        else:
            print(f"weight = {weightnum}, height = {height} BMI: {imc:.2f} — Obese")
