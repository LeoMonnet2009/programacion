import sqlite3

class Estudiantes:
    
    def __init__(self, nombre, edad, año_id):
        self.nombre = nombre
        self.edad = edad
        self.año_id = año_id
        
    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        
        c.execute('INSERT INTO Estudiantes (nombre, edad, año_id) VALUES (?)',
                  (self.nonbre, self.edad, self.año_id))
        
        conn.commit()
        conn.close()
        
    @staticmethod
    def obtener_estudiantes():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM Estudiantes')
        estudiante = c.fetchall()
        conn.close()
        
        return Estudiantes