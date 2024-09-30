def crear_futbolista():
    
    print("Futbolista creado!")

def crear_arquero():
    
    print("Arquero creado!")

def jugar():
    if futbolista and arquero:
        
        print("¡Comienza el partido!")
    else:
        print("Debes crear un Futbolista y un Portero para jugar")

futbolista = None
arquero = None

while True:
    print("Menú:")
    print("1. Crear Futbolista")
    print("2. Crear Arquero")
    print("3. Jugar")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        crear_futbolista()
    elif opcion == '2':
        crear_arquero()
    elif opcion == '3':
        jugar()
    elif opcion == '4':
        break
    else:
        print("Opción inválida")
        
    def crear_futbolista():
        global futbolista
    nombre = input("Ingrese el nombre del futbolista: ")
    ritmo = int(input("Ingrese la habilidad de ritmo (1-99): "))
    tiro = int(input("Ingrese la habilidad de tiro (1-99): "))
    pase = int(input("Ingrese la habilidad de pase (1-99): "))
    regate = int(input("Ingrese la habilidad de regate (1-99): "))
    defensa = int(input("Ingrese la habilidad de defensa (1-99): "))
    fisico = int(input("Ingrese la habilidad física (1-99): "))

    futbolista = {
        "nombre": nombre,
        "tiro": tiro,
        "pase": pase,
        "regate": regate,
        "defensa": defensa,
        "fisico": fisico
    }
    print(f"¡{nombre} ha sido creado")
    
    def crear_arquero():
        global arquero
    nombre = input("Ingrese el nombre del arquero: ")
    salida = int(input("Ingrese la habilidad de salida (1-99): "))
    parada = int(input("Ingrese la habilidad de parada (1-99): "))
    saque = int(input("Ingrese la habilidad de saque (1-99): "))
    reflejos = int(input("Ingrese la habilidad de reflejos (1-99): "))
    velocidad = int(input("Ingrese la habilidad de velocidad (1-99): "))
    posicionamiento = int(input("Ingrese la habilidad de posicionamiento (1-99): "))

    arquero = {
        "nombre": nombre,
        "salida": salida,
        "parada": parada,
        "saque": saque,
        "reflejos": reflejos,
        "velocidad": velocidad,
        "posicionamiento": posicionamiento
    }
