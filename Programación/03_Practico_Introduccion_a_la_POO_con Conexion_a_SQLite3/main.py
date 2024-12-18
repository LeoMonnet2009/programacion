import sqlite3
from class_estudiante import Estudiantes
from class_profesor import Profesores
from class_materia import Materias
from class_calificacion import Calificaciones

def conectar_db():
    conn = sqlite3.connect('escuela.db')
    

def main (): 
    conn = conectar_db()
    cursor = conn.cursor()
    
    while True:
        print("\nSistema de Gestion Escolar")
        print("1. Aregar estudiante")
        print("2. Aregar profesor")
        print("3. Agregar materia")
        print("4. Agregar calificacion")
        print("5. Mostrar estudiantes")
        print("6. Mostrar profesores")
        print("7. Mostrar materias") 
        print("8. Mostrar calificaciones")
        print("9. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            Estudiantes.agregar(conn, nombre, edad)
        elif opcion == '2':
            nombre = input("Nombre del profesor")
            edad = input("Edad del profesor")
            Profesores.agregar(conn, nombre, edad)
        elif opcion == '3':
            nombre = input("Nombre de la materia")
            Materias.agregar(conn, nombre)
        elif opcion == '4':
            id_esutudiante = input("Nombre de la materia")
            id_materia = input("ID de la materia")
            nota = input("calificacion")
        elif opcion == '5':
            Estudiantes.mostrar_todos(conn)
        elif opcion == '6':
            Profesores.mostrar_todos(conn)
        elif opcion == '7':
            Materias.mostrar_todas(conn)
        elif opcion == '8':
            Calificaciones.mostrar_todas(conn)
        elif opcion == '9':
            print("Saliendo del sistema")
            break
        else:
            print("Opcion no valida, intente nuevamente")
            
            conn.close()
        
if __name__ == "__main__":
    main()