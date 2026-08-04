#Este codigo simula un Pise con un sistema de 3 roles 
usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'nmiguel': {'password': '1234', 'rol': 'alumno', 'nombre':'Miguel Navarrete' },
    'sluis': {'password': '1234', 'rol': 'alumno', 'nombre': 'Luis Solano'},
    'ahitler':{'password': '1234', 'rol': 'alumno', 'nombre': 'Alfonso Hitler'},    #Usuarios (6 alumnos, 1 profesor, 1 cordinador)
    'kana': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Ku'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}
materias = ('Matemáticas', 'Programación', 'Inglés') #Materias 

calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 7.0},
    'nmiguel': {'Matemáticas': 6.0, 'Programación': 8.0, 'Inglés': 9.5}, #Calificaciones
    'sluis': {'Matemáticas': 5.0, 'Programación': 6.0, 'Inglés': 8.5},
    'ahitler': {'Matemáticas': 8.0, 'Programación': 7.0, 'Inglés': 7.5},
    'kana': {'Matemáticas': 7.0, 'Programación': 9.0, 'Inglés': 8.0},
}
usuario = None  #Sistema de login
Login_correcto = False
intentos =0
while not Login_correcto: #Empieza el sistema de login con el ciclo while
    print("SISTEMA DE GESTIÓN ESCOLAR")
    usuario_input = input("Usuario: ")
    password_input = input("Contraseña: ")

    if usuario_input in usuarios and usuarios[usuario_input]['password'] == password_input:
        Login_correcto = True
        usuario = usuario_input
        nombre_usuario = usuarios[usuario]['nombre']
        rol_usuario = usuarios[usuario]['rol']
        print(f"\nBienvenido, {nombre_usuario} ({rol_usuario})\n")
    else:
        print("Usuario o contraseña incorrectos. Intente de nuevo.\n")
        intentos=intentos+1
        print(f"Numeros de intentos: ",{intentos})

if rol_usuario == 'alumno': #Cuando los usuarios concide con el alumno
    print(f"Boleta de {nombre_usuario}")
    aprobadas = set()
    for materia in materias:
        calificacion = calificaciones[usuario][materia]
        print(f"{materia}: {calificacion}")
        if calificacion >= 8.0:
            aprobadas.add(materia)
            
    pendientes = set(materias) - aprobadas  # Calcular materias pendientes usando diferencia de conjuntos
    
    print(f"Materias aprobadas: {aprobadas}") 
    print(f"Materias pendientes: {pendientes}")

elif rol_usuario == 'maestro':
    print("ALUMNOS REGISTRADOS")
    for usuario, datos in usuarios.items():
        if datos['rol'] == 'alumno':
            print(f"- {usuario}: {datos['nombre']}")
            
    print("\nEDICIÓN DE CALIFICACIONES")
    alumno_target = input("Alumno (username): ")
    
    if alumno_target in usuarios and usuarios[alumno_target]['rol'] == 'alumno':     # Validación simple de existencia del alumno
        materia = input("Materia: ")
        
        if materia in materias:
            nvcalificacion = float(input("Nueva calificación: "))
            calificaciones[alumno_target][materia] = nvcalificacion
            print("Calificación actualizada.")
        else:
            print("Error: La materia ingresada no existe")
    else:
        print("Error: El usuario no es un alumno valido")

elif rol_usuario == 'coordinador': #vista del cordinador
    print("REPORTE GENERAL DEL SISTEMA \n")
    print("--- Maestros ---")
    for usuario, datos in usuarios.items():
        if datos['rol'] == 'maestro':
            print(f"- {datos['nombre']} ({usuario})")
            
    print("\n--- Materias ---")  #Lista de materias
    for materia in materias:
        print(f"- {materia}")
        
    print("\n--- Alumnos y Calificaciones ---") #lista de los alumnos y sus calificaciones completas
    for alumno, materias_map in calificaciones.items():
        nombre_alumno = usuarios[alumno]['nombre']
        print(f"\nAlumno: {nombre_alumno} ({alumno})")
        for materia in materias:
            print(f"  {materia}: {materias_map[materia]}")