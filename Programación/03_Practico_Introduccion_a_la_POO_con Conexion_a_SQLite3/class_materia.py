import sqlite3

class Materias:
    
    def __init__(self, nombre, edad, año_id):
        self.nombre = nombre
                
    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        
        c.execute('INSERT INTO Materias (nombre) VALUES (?)',
                  (self.nonbre))
        
        conn.commit()
        conn.close()
        
    @staticmethod
    def obtener_estudiantes():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM Materias')
        estudiante = c.fetchall()
        conn.close()
        
        return Materias