from soldados import Soldado
from gemas import Gema
from armas import Arma
import json
import os 

dir_act = os.path.abspath(os.path.dirname(__file__))
menu ='''
Escoja una opción:
    1)Agregar un Soldado.
    2)Agregar Gema.
    3)Agregar Arma.
    4)Agregar Dinastia.
    5)Salir.

Utilize el numero correspondiente para seleccionar la accion.
> '''

print('Bienvenido a el pergamino de c-sharp')

while True:
    print("".center(50,"-"))
    opcion=input(menu)
    print("".center(50,"-"))

    if opcion=='1':
        print("Ha seleccionado la opcion 1.")
        print("".center(50,"-"))
        #Valida si la entrada es numerica 
        
        apodo = input(f"Ingrese el Apodo del soldado : ")
        tipoarma = input("Tipo de arma (Cuchillos, Lanzas, Martillos, Espadas): ")
        ubicacion = input("Ubicacion en la formación (1...n): ")
        dinastia = input("Dinastía (swift, flutter, java): ")
        #Valida si la entrada es valida
        while True:
            gem = input("Posee gemas? (si/no): ")
            if gem == "si":
                gems=True
                break
            elif gem == "no":
                gems=False
                break
            else:
                print("Entrada no valida")
        soldado = Soldado(apodo,gems,tipoarma,ubicacion,dinastia)

        while True:
            na = input("Numero de armas: ")
            n = int(na)
            if na.isnumeric and n>0:
                print("".center(50,"-"))
                for j in range(1,n+1):
                    arma = input(f"Arma #{j} de tipo {soldado.tipoarma}: ")
                    soldado.armas_name.append(arma)
                print("".center(50,"-"))
                break
            elif n==0:
                pass
            else:
                print("Entrada no valida")
        
        if os.path.exists(f"{dir_act}/bd/people/info.json"):
            with open(f"{dir_act}/bd/people/info.json","r") as j:
                data = json.load(j)

            data['soldados'].append({
            'apodo': soldado.apodo,
            'gemas': [x for x in  soldado.gem_name],
            'tipoarma': soldado.tipoarma,
            'armas': [x for x in  soldado.armas_name],
            'ubicacion': soldado.ubicacion,
            'dinastia': soldado.dinastia 
            })

            dir =  f"{dir_act}/bd/people"
            filename = "info.json"
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            soldados = {}
            soldados['soldados'] = []
            
            #Agrega los soldados con sus detalles al diccionario
            soldados['soldados'].append({
            'apodo': soldado.apodo,
            'gemas': [x for x in  soldado.gem_name],
            'tipoarma': soldado.tipoarma,
            'armas': [x for x in  soldado.armas_name],
            'ubicacion': soldado.ubicacion,
            'dinastia': soldado.dinastia 
            })
            #Se define la ruta donde se creará el json
            dir =  f"{dir_act}/bd/people"
            filename = "info.json"  
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(soldados, file, indent=4)
        #Se crea el diccionario para las gemas por soldado si posee gemas
        if gems==True:
            gemas = {}
            gemas[f'{soldado.apodo}'] = []
            
            #Recorre el numero de gemas que tiene el soldado y los agrega al diccionario
            gemas[f'{soldado.apodo}'].append({
                f'gemas': [x for x in  soldado.gem_name] }) 

            #Se define la ruta donde se creará el json
            os.makedirs(f"{dir_act}/bd/people/{soldado.apodo}", exist_ok=True)  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
            dir =  f"{dir_act}/bd/people/{soldado.apodo}"
            filename = "gemas.json" 

            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(gemas, file, indent=4)
        
        
    elif opcion == '2':
        print("Ha seleccionado la opcion 2.")
        print("".center(50,"-"))
                
        tipo = input(f"Ingrese el tipo de la gema: ")
        poder = input(f"Ingrese el poder de la gema: ")
        tipoarma = input(f"Tipo de arma valida para la gema: ")
        #Valida si la entrada es valida
        gema = Gema(tipo,poder,tipoarma)

        dir =  f"{dir_act}/bd/gemas"
        filename = "gemasinfo.json"
        if os.path.exists(f"{dir_act}/bd/gemas/gemasinfo.json"):
            with open(f"{dir_act}/bd/gemas/gemasinfo.json","r") as j:
                data = json.load(j)

            print(data)
            data['gemas'].append({
            'tipo': gema.tipo,
            'poder': gema.poder,
            'tipoarma': gema.tipoarma 
            })

               
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            gemas = {}
            gemas['gemas'] = []
            
            #Agrega las gemas con sus detalles al diccionario
            gemas['gemas'].append({
                'tipo': gema.tipo,
                'poder': gema.poder,
                'tipoarma': gema.tipoarma 
                }) 
            #Se define la ruta donde se creará el json
              
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(gemas, file, indent=4)
            
            
        gemas = {}
        gemas[f'{gema.tipo}'] = []
        
        #Recorre el numero de gemas que tiene el soldado y los agrega al diccionario
        gemas[f'{gema.tipo}'].append({
            'tipo': gema.tipo,
            'poder': gema.poder,
            'tipoarma': gema.tipoarma  
            }) 

        #Se define la ruta donde se creará el json
        os.makedirs(f"{dir_act}/bd/gemas/{gema.tipo}", exist_ok=True)  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
        dir =  f"{dir_act}/bd/gemas/{gema.tipo}"
        filename = f"{gema.tipo}info.json" 

        with open(os.path.join(dir,filename), 'w') as file:
            json.dump(gemas, file, indent=4)

        print("".center(50,"-"))

    elif opcion == '3':
        print("Ha seleccionado la opcion 3.")
        print("".center(50,"-"))

        #def __init__(self, nombre, poder, posicion):        
        tipo = input(f"Ingrese el tipo de arma: ")
        nombre = input(f"Ingrese el nombre del arma: ")
        poder = input(f"Ingrese el poder del arma: ")
        posicion = input(f"Posicion en la que el arma debe ser usada: ")
        
        arma = Arma(nombre,poder,posicion)

        dir =  f"{dir_act}/bd/arma"
        filename = "armasinfo.json"
        if os.path.exists(f"{dir_act}/bd/arma/armasinfo.json"):
            with open(f"{dir_act}/bd/arma/armasinfo.json","r") as j:
                data = json.load(j)

            print(data)
            data['armas'].append({
            'nombre': arma.nombre,
            'poder': arma.poder,
            'posicion': arma.posicion 
            })
 
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            armas = {}
            armas['armas'] = []
            
            #Agrega las armas con sus detalles al diccionario
            armas['armas'].append({
            'nombre': arma.nombre,
            'poder': arma.poder,
            'posicion': arma.posicion 
            })
            #Se define la ruta donde se creará el json
              
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(armas, file, indent=4)
            
            
    
        dir =  f"{dir_act}/bd/arma/{tipo}"
        filename = "armasinfo.json"
        if os.path.exists(f"{dir_act}/bd/arma/{tipo}/armasinfo.json"):
            with open(f"{dir_act}/bd/arma/{tipo}/armasinfo.json","r") as j:
                data = json.load(j)

            print(data)
            data['armas'].append({
            'nombre': arma.nombre,
            'poder': arma.poder,
            'posicion': arma.posicion 
            })
 
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            armas = {}
            armas['armas'] = []
            
            #Agrega las armas con sus detalles al diccionario
            armas['armas'].append({
            'nombre': arma.nombre,
            'poder': arma.poder,
            'posicion': arma.posicion 
            })
            #Se define la ruta donde se creará el json
            os.makedirs(f"{dir_act}/bd/arma/{tipo}", exist_ok=True)  
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(armas, file, indent=4)

        print("".center(50,"-"))

    elif opcion == '5':
        print("Hasta pronto")
        break
    else:
        print("Entrada no valida, digite un numero del menú")



