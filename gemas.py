class Gema:
    
    def __init__(self, tipo, poder, tipoarma):
        
        self.tipo=tipo
        self.poder=poder
        self.tipoarma=tipoarma

    def __str__(self):
        return f"Tipo: {self.tipo} / Poder: {self.poder} / Tipo de Arma: {self.tipoarma} "
        



