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
            while True:
                ng = input("\nNumero de gemas: ")
                n = int(ng)
                if ng.isnumeric() and n>0:
                    print("".center(50,"-"))
                    for i in range(1,n+1):
                        gema = input(f"Gema #{i}: ")
                        self.gem_name.append(gema)
                    print("".center(50,"-"))
                    break
                else:
                    print("La entrada debe ser un numero entero mayor a 0")
        
        
                

    def __str__(self):
        return f"Apodo: {self.apodo} / Posee gemas: {self.gemas} / Arma: {self.tipoarma} / Ubicacion: {self.ubicacion} / Dinastia: {self.dinastia}"



