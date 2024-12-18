class Personaje:
    estado = True 

    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza

    def atacar(self, otro_personaje):
        daño = self.fuerza - otro_personaje.resistencia
        if daño > 0:
            otro_personaje.recibir_dano(daño)
            print(f"{self.nombre} infligió {daño} puntos de daño a {otro_personaje.nombre}")
        else:
            print(f"{self.nombre} no pudo infligir daño a {otro_personaje.nombre}")

    def recibir_dano(self, cantidad):
        self.resistencia -= cantidad
        if self.resistencia <= 0:
            self.estado = False
            print(f"{self.nombre} ha sido derrotado!")

    def mostrar_info(self):
        estado = "vivo" if self.estado else "muerto"
        print(f"Nombre: {self.nombre}")
        print(f"Altura: {self.altura} m")
        print(f"Velocidad: {self.velocidad} m/s")
        print(f"Resistencia: {self.resistencia}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Estado: {estado}")