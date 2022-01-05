from soldados import Soldado
import json
import os 

dir_act = os.path.abspath(os.path.dirname(__file__))
lista_soldados = []

menu ='''
Escoja una opción:
    1)Agregar un Soldado.
    2)XXXXXXXX.
    3)Salir.
Utilize el numero correspondiente para seleccionar la accion.
> '''

print('Bienvenido a el pergamino de c-sharp')

while True:
    print("".center(50,"-"))
    opcion=int(input(menu))
    print("".center(50,"-"))
    
    if opcion==1:
        print("Ha seleccionado la opcion 1.")
        print("".center(50,"-"))
        n = int(input("Numero de Soldados a Agregar: "))
        if n>0:
            for i in range(1,n+1):
                apodo = input(f"Ingrese el Apodo del soldado #{i}: ")
                gem = input("Posee gemas? (si/no): ")
                if gem == "si":
                    gems=True
                elif gem == "no":
                    gems=False
                else:
                    print("Entrada no valida")
                    break
                tipoarma = input("Tipo de arma (Cuchillos, Lanzas, Martillos, Espadas): ")
                ubicacion = int(input("Ubicacion en la formación (1...n): "))
                dinastia = input("Dinastía (swift, flutter, java): ")
                
                soldado = Soldado(apodo,gems,tipoarma,ubicacion,dinastia)
                lista_soldados.append(soldado)

                #Se crea el diccionario para las gemas por soldado si posee gemas
                if gems==True:
                    gemas = {}
                    gemas[f'{lista_soldados[i-1].apodo}'] = []
                    
                    #Recorre el numero de gemas que tiene el soldado y los agrega al diccionario
                    gemas[f'{lista_soldados[i-1].apodo}'].append({
                        f'gemas': [x for x in  lista_soldados[i-1].gem_name] }) 

                    #Se define la ruta donde se creará el json
                    os.makedirs(f"{dir_act}/bd/people/{lista_soldados[i-1].apodo}", exist_ok=True)  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
                    dir =  f"{dir_act}/bd/people/{lista_soldados[i-1].apodo}"
                    filename = "gemas.json" 

                    with open(os.path.join(dir,filename), 'w') as file:
                        json.dump(gemas, file, indent=4) 


