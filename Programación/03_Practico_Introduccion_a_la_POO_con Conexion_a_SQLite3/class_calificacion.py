import sqlite3

class Calificaciones:
    
    def __init__(self, calificacion):
        self.calificacion = calificacion
                
    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        
        c.execute('INSERT INTO Calificaciones (nombre) VALUES (?)',
                  (self.calificacion))
        
        conn.commit()
        conn.close()
        
    @staticmethod
    def obtener_estudiantes():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM Calificaciones')
        estudiante = c.fetchall()
        conn.close()
        
        return Calificaciones