class Arma:
    
    def __init__(self, nombre, poder, posicion):
        
        self.nombre=nombre
        self.poder=poder
        self.posicion=posicion

    def __str__(self):
        return f"Nombre: {self.nombre} / Poder: {self.poder} / Posicion: {self.posicion} "
        



