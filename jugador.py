

class Jugador:
    def __init__(self,nombre,puntos,tiempo) -> None:
        self.nombre = nombre
        self.puntos = puntos 
        self.tiempo = tiempo
    
    def sumar_puntos(self,puntos):
        self.puntos += puntos
    
    def sumar_tiempo(self):
        self.tiempo += 1