#Evaluate grade using while
end="done"
grade=""
count=0
gradeave=0 
result=0
while grade != end: #Aqui iniciamos el clico para recolectar data
    grade=input("Ingrese la calificacion, si desea terminar ingrese 'done'")
    if grade !=end:
        gradeave=gradeave+float(grade)
        count= count+1
    if grade.lower()=="done":
        break #Aqui el ciclo termina si el usuario usa "done" 
if gradeave==0: #Aqui para corregir el error y inicio el ciclo if por que no se puede una division entre 0
    print("Please enter almost one grade") 
else:
    result=gradeave/count #Promedio final y validacion de los resultados si es aprobatorio o no
    if result<7:
        print("Student failed: ")
        print(result)   
    else:
        print("Stundent pass: ")
        print(result)        