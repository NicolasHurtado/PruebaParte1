from dinastias import Dinastia
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
    4)Agregar Dinastía.
    5)Agregar Posicion en la formacion del ejercito.
    6)Salir.

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
        
        armas_name = []
        gem_name = []
        apodo = input(f"Ingrese el Apodo del soldado : ")
        tipoarma = input("Tipo de arma (Cuchillos, Lanzas, Martillos, Espadas): ")
        ubicacion = input("Ubicacion en la formación (1...n): ")
        dinastia = input("Dinastía (swift, flutter, java): ")
        #Valida si la entrada es valida
        while True:
            gem = input("Posee gemas? (si/no): ")
            if gem == "si":
                gems=True
                while True:
                    try:
                        ng = input("\nNumero de gemas: ")
                        n = int(ng)
                        print("".center(50,"-"))
                        for i in range(1,n+1):
                            gema = input(f"Gema #{i}: ")
                            gem_name.append(gema)
                        print("".center(50,"-"))
                        break
                    except:
                        print("La entrada debe ser un numero entero mayor a 0")
                break
            elif gem == "no":
                gems=False
                break
            else:
                print("Entrada no valida")

        while True:
            try:
                n = int(input("Numero de armas: "))
                if n>0:
                    print("".center(50,"-"))
                    for j in range(1,n+1):
                        arma = input(f"Arma #{j} de tipo {tipoarma}: ")
                        armas_name.append(arma)
                    print("".center(50,"-"))
                    break
            except:
                print("Entrada no valida")
        
        dir =  f"{dir_act}/bd/people"
        filename = "soldadosinfo.json"

        if os.path.exists(f"{dir}/{filename}"):
            with open(f"{dir}/{filename}","r") as j:
                data = json.load(j)

            
            #Recorre la data, si encuentra un soldado que ya esté creado, lo elimina y lo vuelve a crear para no duplicar el registro
            for i in range(len(data)):
                if data["soldados"][i]["apodo"]==apodo:
                    del data["soldados"][i]
                else:
                    pass
            
            data['soldados'].append({
                'apodo': apodo,
                'poseegemas': gems,
                'gemas': [x for x in  gem_name],
                'tipoarma': tipoarma,
                'armas': [x for x in  armas_name],
                'ubicacion': int(ubicacion),
                'dinastia': dinastia 
                })
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            soldados = {}
            soldados['soldados'] = []
            
            #Agrega los soldados con sus detalles al diccionario
            soldados['soldados'].append({
            'apodo': apodo,
            'poseegemas': gems,
            'gemas': [x for x in  gem_name],
            'tipoarma': tipoarma,
            'armas': [x for x in  armas_name],
            'ubicacion': int(ubicacion),
            'dinastia': dinastia 
            })
            #Se define la ruta donde se creará el json  
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(soldados, file, indent=4)

        #Se crea el diccionario para las gemas por soldado si posee gemas
        if gems==True:
            gemas = {}
            gemas[f'{apodo}'] = []
            
            #Recorre el numero de gemas que tiene el soldado y los agrega al diccionario
            gemas[f'{apodo}'].append({
                f'gemas': [x for x in  gem_name] }) 

            #Se define la ruta donde se creará el json
            os.makedirs(f"{dir_act}/bd/people/{apodo}", exist_ok=True)  
            dir =  f"{dir_act}/bd/people/{apodo}"
            filename = "gemas.json" 

            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(gemas, file, indent=4)
            

        #Se crearán las combinaciones de los poderes del soldado

        
        combinaciones = {}
        combinaciones['combinaciones'] = []
        
        #Agrega los soldados con sus detalles al diccionario
        combinaciones['combinaciones'].append({
        'apodo': apodo,
        'poseegemas': gems,
        'gemas': [x for x in  gem_name],
        'tipoarma': tipoarma,
        'armas': [x for x in  armas_name],
        'ubicacion': int(ubicacion),
        'dinastia': dinastia 
        })
        #Se define la ruta donde se creará el json
        os.makedirs(f"{dir_act}/bd/people/{apodo}/combinaciones", exist_ok=True)
        dir =  f"{dir_act}/bd/people/{apodo}/combinaciones"
        filename = "combination.json"   
        with open(os.path.join(dir,filename), 'w') as file:
            json.dump(combinaciones, file, indent=4)
        
        
    elif opcion == '2':
        print("Ha seleccionado la opcion 2.")
        print("".center(50,"-"))
                
        tipo = input(f"Ingrese el tipo de la gema: ")
        poder = input(f"Ingrese el poder de la gema: ")
        tipoarma = input(f"Tipo de arma valida para la gema: ")
        #Valida si la entrada es valida

        dir =  f"{dir_act}/bd/gemas"
        filename = "gemasinfo.json"
        if os.path.exists(f"{dir}/{filename}"):
            with open(f"{dir}/{filename}","r") as j:
                data = json.load(j)
            
            #Recorre la data, si encuentra una gema que ya esté creado, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data)):
                if data["gemas"][i]["tipo"]==tipo:
                    del data["gemas"][i]
                else:
                    pass

            data['gemas'].append({
            'tipo': tipo,
            'poder': poder,
            'tipoarma': tipoarma 
            })
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
            
        else:
            gemas = {}
            gemas['gemas'] = []
            
            #Agrega las gemas con sus detalles al diccionario
            gemas['gemas'].append({
                'tipo': tipo,
                'poder': poder,
                'tipoarma': tipoarma 
                }) 
            #Se define la ruta donde se creará el json
              
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(gemas, file, indent=4)
            
            
        gemas = {}
        gemas[f'{tipo}'] = []
        
        #Recorre el numero de gemas que tiene el soldado y los agrega al diccionario
        gemas[f'{tipo}'].append({
            'tipo': tipo,
            'poder': poder,
            'tipoarma': tipoarma  
            }) 

        #Se define la ruta donde se creará el json
        os.makedirs(f"{dir_act}/bd/gemas/{tipo}", exist_ok=True)  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
        dir =  f"{dir_act}/bd/gemas/{tipo}"
        filename = f"{tipo}info.json" 

        with open(os.path.join(dir,filename), 'w') as file:
            json.dump(gemas, file, indent=4)

        print("".center(50,"-"))

    elif opcion == '3':
        print("Ha seleccionado la opcion 3.")
        print("".center(50,"-"))
     
        tipo = input(f"Ingrese el tipo de arma: ")
        nombre = input(f"Ingrese el nombre del arma: ")
        poder = input(f"Ingrese el poder del arma: ")
        posicion = input(f"Posicion en la que el arma debe ser usada: ")
        
        dir =  f"{dir_act}/bd/arma"
        filename = "armasinfo.json"
        if os.path.exists(f"{dir}/{filename}"):
            with open(f"{dir}/{filename}","r") as j:
                data = json.load(j)

            #Recorre la data, si encuentra un arma que ya esté creada, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data)):
                if data["armas"][i]["nombre"]==nombre:
                    del data["armas"][i]
                else:
                    pass

            data['armas'].append({
            'tipo': tipo,
            'nombre': nombre,
            'poder': poder,
            'posicion': int(posicion) 
            })
 
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            armas = {}
            armas['armas'] = []
            
            #Agrega las armas con sus detalles al diccionario
            armas['armas'].append({
            'tipo': tipo,
            'nombre': nombre,
            'poder': poder,
            'posicion': posicion 
            })
            #Se define la ruta donde se creará el json
              
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(armas, file, indent=4)
            
            
    
        dir =  f"{dir_act}/bd/arma/{tipo}"
        filename = "armasinfo.json"
        if os.path.exists(f"{dir}/{filename}"):
            with open(f"{dir}/{filename}","r") as j:
                data = json.load(j)

            #Recorre la data, si encuentra una arma que ya esté creada, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data)):
                if data[f'{tipo}'][i]["nombre"]==nombre:
                    del data[f'{tipo}'][i]
                else:
                    pass

            data[f'{tipo}'].append({
            'nombre': nombre,
            'poder': poder,
            'posicion': int(posicion) 
            })
 
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            armas = {}
            armas[f'{tipo}'] = []
            
            #Agrega las armas con sus detalles al diccionario
            armas[f'{tipo}'].append({
            'nombre': nombre,
            'poder': poder,
            'posicion': int(posicion) 
            })
            #Se define la ruta donde se creará el json
            os.makedirs(f"{dir_act}/bd/arma/{tipo}", exist_ok=True)  
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(armas, file, indent=4)

        print("".center(50,"-"))
    elif opcion == '4':
        print("Ha seleccionado la opcion 4.")
        print("".center(50,"-"))

        poderes = []
        nombre = input(f"Ingrese el nombre de la dinastía: ")
        
        
        while True:
            n = input(f"Cantidad de Posiciones de la dinastía {nombre}: ")
            if n.isnumeric() and int(n)>0:
                print("".center(50,"-"))
                for j in range(1,int(n)+1):
                    while True:
                        pos = input(f"Posicion #{j} de la dinastía {nombre}: ")
                        if pos.isnumeric() and int(pos)>=0:
                            posi = int(pos)
                            pod = input(f"Suma total del poder de la dinastía {nombre} en la posicion {pos}:  ")
                            if pod.isnumeric() and int(pod)>=0:
                                podf = int(pod)
                                trupla = (posi,podf)
                                poderes.append(trupla)
                                print("".center(50,"-"))
                                break
                            else:
                                print("\nLa suma total del poder debe ser un numero mayor o igual a 0\n")
                        else:
                            print("La posicion debe ser un numero entero mayor o igual a 0")
                print("".center(50,"-"))
                break
            elif n==0:
                print("Debes tener almenos una posicion para la dinastía")
            else:
                print("Entrada no valida")

        dir =  f"{dir_act}/bd/arma"
        filename = "dinastiasinfo.json"
        if os.path.exists(f"{dir}/{filename}"):
            with open(f"{dir}/{filename}","r") as j:
                data = json.load(j)

            #Recorre la data, si encuentra una dinastía que ya esté creada, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data)):
                if data["dinastias"][i]["nombre"]==nombre:
                    del data["dinastias"][i]
                else:
                    pass

            data['dinastias'].append({
            'nombre': nombre,
            'poder': [x for x in poderes]
            })
 
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            dinastias = {}
            dinastias['dinastias'] = []
            
            #Agrega las dinastias con sus detalles al diccionario
            dinastias['dinastias'].append({
            'nombre': nombre,
            'poder': [x for x in poderes]
            })
            #Se define la ruta donde se creará el json
              
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(dinastias, file, indent=4)
            
        
        dinastias = {}
        dinastias[f'{nombre}'] = []
        
        #Agrega las dinastias con sus detalles al diccionario
        dinastias[f'{nombre}'].append({
            'nombre': nombre,
            'poder': [x for x in poderes]
            })
        #Se define la ruta donde se creará el json
        os.makedirs(f"{dir_act}/bd/arma/dinastia_{nombre}", exist_ok=True) 
        dir =  f"{dir_act}/bd/arma/dinastia_{nombre}"
        filename = f"{nombre}info.json" 
        with open(os.path.join(dir,filename), 'w') as file:
            json.dump(dinastias, file, indent=4)

        print("".center(50,"-"))
    elif opcion == '5':
        print("Ha seleccionado la opcion 5.")
        print("".center(50,"-"))

        while True:
            try:
                pos = int(input(f"Ingrese la posicion en la formacion del ejercito : "))
                if pos:
                    print("".center(50,"-"))
                    while True:
                        try:
                            pod = int(input(f"Ingrese la suma del poder de la posicion {pos}: "))
                            if pod>=0:
                                print("Posicion creada")
                                break
                        except:
                            print("La suma del poder debe ser mayor o igual a 0")
                    print("".center(50,"-"))
                    break
            except:
                print("La posicion debe ser un numero entero")
                

            
            

        dir =  f"{dir_act}/bd/arma"
        filename = "positioninfo.json"
        if os.path.exists(f"{dir_act}/bd/arma/{filename}"):
            with open(f"{dir_act}/bd/arma/{filename}","r") as j:
                data = json.load(j)

            #Recorre la data, si encuentra una posición que ya esté creada, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data)):
                if data["posiciones"][i]["posicion"]==pos:
                    del data["posiciones"][i]
                else:
                    pass
            data['posiciones'].append({
            'posicion': pos,
            'poder': pod
            })
 
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            posiciones = {}
            posiciones['posiciones'] = []
            
            #Agrega las dinastias con sus detalles al diccionario
            posiciones['posiciones'].append({
            'posicion': pos,
            'poder': pod
            })
            #Se define la ruta donde se creará el json
              
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(posiciones, file, indent=4)
            
        
        posiciones = {}
        posiciones[f'{pos}'] = []
        
        #Agrega las posiciones con sus detalles al diccionario
        posiciones[f'{pos}'].append({
            'posicion': pos,
            'poder': pod
            })
        #Se define la ruta donde se creará el json
        dir =  f"{dir_act}/bd/arma/position{pos}"
        filename = f"position{pos}info.json"
        os.makedirs(f"{dir_act}/bd/arma/position{pos}", exist_ok=True)  
        with open(os.path.join(dir,filename), 'w') as file:
            json.dump(posiciones, file, indent=4)

    elif opcion == '6':
        print("Hasta pronto")
        break
    else:
        print("Entrada no valida, digite un numero del menú")



