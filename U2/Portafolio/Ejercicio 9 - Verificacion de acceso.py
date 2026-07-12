
#Problema 9:
  #El sistema guarda el usuario "admin" y la contrasena "1234". Lee un
  #usuario y una contrasena. Primero verifica el usuario; solo si es
  #correcto, verifica la contrasena. Imprime "Bienvenido",
  #"Contrasena incorrecta" o "Usuario desconocido".
user= input("Ingresa el usuario: ")
if user =="admin":
    print("Bienvenido admin")
    pas=int(input("Ingrese la contraseña: "))
    if pas == 1234:
        print("Bienvendio al sitema xxx")