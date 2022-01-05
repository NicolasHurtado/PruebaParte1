class Soldado:
    
    def __init__(self, apodo=None, gemas=False, tipoarma=None, ubicacion=None,dinastia=None):
        self.gem_name = []
        self.armas_name = []
        self.apodo=apodo
        self.gemas=gemas
        self.tipoarma=tipoarma
        self.ubicacion=ubicacion
        self.dinastia=dinastia

        if self.gemas == True:
            n = int(input("Numero de gemas: "))
            for i in range(1,n+1):
                gema = input(f"Gema #{i}: ")
                self.gem_name.append(gema)
        
        n = int(input("Numero de armas: "))

        if n>0:
            for i in range(1,n+1):
                    arma = input(f"Arma #{i} de tipo {self.tipoarma}: ")
                    self.armas_name.append(arma)
        else:
            pass
                

    def __str__(self):
        return f"Apodo: {self.apodo} / Posee gemas: {self.gemas} / Arma: {self.tipoarma} / Ubicacion: {self.ubicacion} / Dinastia: {self.dinastia}"



