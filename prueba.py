import json
import os 

dir_act = os.path.abspath(os.path.dirname(__file__))
menu ='''
Escoja una opción:
    1) Agregar o Editar Soldado.
    2) Agregar o Editar Gema.
    3) Agregar o Editar Arma.
    4) Agregar o Editar Dinastía.
    5) Agregar o Editar Posicion en la formacion del ejercito.
    6) Mostrar la combinación con el maximo poder.
    7) Salir.

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
        apodo = input(f"Ingrese el Apodo del soldado : ").capitalize()
        while True:
            tipoarma = input("Tipo de arma (Cuchillos, Lanzas, Martillos, Espadas): ").capitalize()
            if tipoarma=="Cuchillos" or tipoarma=="Lanzas" or tipoarma=="Martillos" or tipoarma=="Espadas":
                break
            else:
                print("\nTipo de arma no valida.\n")
        
        while True:
            try:
                ubicacion = int(input("Ubicacion en la formación (1...n): "))
                if ubicacion>=0:
                    break
                else:
                    print("\nNo puede ser un numero negativo.\n")
            except:
                print("\nLa ubicacion debe ser un numero entero mayor o igual a 0.\n")

        while True:
            dinastia = input("Dinastía (swift, flutter, java): ").capitalize()
            if dinastia=="Swift" or dinastia=="Flutter" or dinastia=="Java":
                break
            else:
                print("\nDinastia no valida.\n")
        #Valida si la entrada es valida
        while True:
            gem = input("Posee gemas? (Si/No): ").capitalize()
            if gem == "Si":
                gems=True
                while True:
                    try:
                        ng = input("\nNumero de gemas: ")
                        n = int(ng)
                        print("".center(50,"-"))
                        for i in range(1,n+1):
                            while True:
                                gema = input(f"Gema #{i} (Onepiece, Hache, Callisto, Backaid, Kaminari): ").capitalize()
                                if gema=="Onepiece" or gema=="Hache" or gema=="Callisto" or gema=="Backaid" or gema=="Kaminari":
                                    break
                                else:
                                    print("\nGema no valida.\n")
                            gem_name.append(gema)
                        print("".center(50,"-"))
                        break
                    except:
                        print("La entrada debe ser un numero entero mayor a 0")
                break
            elif gem == "No":
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
                        arma = input(f"Arma #{j} de tipo {tipoarma}: ").capitalize()
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
            for i in range(len(data["soldados"])):
                if data["soldados"][i]["apodo"]==apodo:
                    del data["soldados"][i]
                    break
                else:
                    pass
            
            data['soldados'].append({
                'apodo': apodo,
                'poseegemas': gems,
                'gemas': [x for x in  gem_name],
                'tipoarma': tipoarma,
                'armas': [x for x in  armas_name],
                'ubicacion': ubicacion,
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
            'ubicacion': ubicacion,
            'dinastia': dinastia 
            })
            #Se define la ruta donde se creará el json  
            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(soldados, file, indent=4)

        
        #Se crearán las combinaciones de los poderes del soldado
        combinaciones = {}
        combinaciones["combinaciones"] = []

        if gems==True:

            #Se crea el diccionario para las gemas por soldado si posee gemas
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
            

            

            #Recorre el arreglo de gemas
            for gema in gem_name:
                #Abre el json donde está la info de las gemas
                dir =  f"{dir_act}/bd/gemas"
                filename = "gemasinfo.json"
                with open(f"{dir}/{filename}","r") as j:
                    datagemas = json.load(j)
                for i in range(len(datagemas["gemas"])):
                    if datagemas["gemas"][i]["tipo"]==gema:
                        podgema = datagemas["gemas"][i]["poder"]
                        break
                    else:
                        podgema=0

                #Recorre el arreglo de armas
                for arma in armas_name:
                    #Abre el json donde está la info de las armas
                    dir =  f"{dir_act}/bd/arma"
                    filename = "armasinfo.json"
                    with open(f"{dir}/{filename}","r") as j:
                        dataarmas = json.load(j)
                    for i in range(len(dataarmas["armas"])):
                        if dataarmas["armas"][i]["nombre"]==arma:
                            podarma = dataarmas["armas"][i]["poder"]
                            break
                        else:
                            podarma = 0
                    
                    #Abre el json donde está la info de las posiciones
                    dir =  f"{dir_act}/bd/arma"
                    filename = "positioninfo.json"
                    with open(f"{dir}/{filename}","r") as j:
                        datapos = json.load(j)
                    for i in range(len(datapos["posiciones"])):
                        if datapos["posiciones"][i]["posicion"]==ubicacion:
                            podpos = datapos["posiciones"][i]["poder"]
                            break
                        else:
                            podpos=0

                    #Abre el json donde está la info de las dinastias
                    dir =  f"{dir_act}/bd/arma"
                    filename = "dinastiasinfo.json"
                    with open(f"{dir}/{filename}","r") as j:
                        datadinas = json.load(j)

                    for i in range(len(datadinas["dinastias"])):
                        if datadinas["dinastias"][i]["nombre"]==dinastia:
                            for poder in datadinas["dinastias"][i]["poder"]:
                                poddinas = poder[1] 
                                print(f"Poder dinastia: {poddinas}")
                                combinaciones["combinaciones"].append({
                                    f"{arma},{str(ubicacion)},{gema},{dinastia}":(podarma+podpos+podgema+poddinas)
                                })   
                        else:
                            pass
            #Se define la ruta donde se creará el json
            os.makedirs(f"{dir_act}/bd/people/{apodo}/combinaciones", exist_ok=True)  
            dir =  f"{dir_act}/bd/people/{apodo}/combinaciones"
            filename = "combination.json" 

            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(combinaciones, file, indent=4)       
        else:
            #Recorre el arreglo de armas
            podgema = 0
            for arma in armas_name:
                #Abre el json donde está la info de las armas
                dir =  f"{dir_act}/bd/arma"
                filename = "armasinfo.json"
                with open(f"{dir}/{filename}","r") as j:
                    dataarmas = json.load(j)
                for i in range(len(dataarmas["armas"])):
                    if dataarmas["armas"][i]["nombre"]==arma:
                        podarma = dataarmas["armas"][i]["poder"]
                        break
                    else:
                        podarma = 0
                
                #Abre el json donde está la info de las posiciones
                dir =  f"{dir_act}/bd/arma"
                filename = "positioninfo.json"
                with open(f"{dir}/{filename}","r") as j:
                    datapos = json.load(j)
                for i in range(len(datapos["posiciones"])):
                    if datapos["posiciones"][i]["posicion"]==ubicacion:
                        podpos = datapos["posiciones"][i]["poder"]
                        break
                    else:
                        podpos=0
                print(f"Poder posicion: {podpos}")
                #Abre el json donde está la info de las dinastias
                dir =  f"{dir_act}/bd/arma"
                filename = "dinastiasinfo.json"
                with open(f"{dir}/{filename}","r") as j:
                    datadinas = json.load(j)

                for i in range(len(datadinas["dinastias"])):
                    if datadinas["dinastias"][i]["nombre"]==dinastia:
                        for poder in datadinas["dinastias"][i]["poder"]:
                            poddinas = poder[1] 
                            print(f"Poder dinastia: {poddinas}")
                            combinaciones["combinaciones"].append({
                                f"{arma},{str(ubicacion)},{dinastia}":(podarma+podpos+podgema+poddinas)
                            })   
                    else:
                        pass
            
            #Se define la ruta donde se creará el json
            os.makedirs(f"{dir_act}/bd/people/{apodo}/combinaciones", exist_ok=True)  
            dir =  f"{dir_act}/bd/people/{apodo}/combinaciones"
            filename = "combination.json" 

            with open(os.path.join(dir,filename), 'w') as file:
                json.dump(combinaciones, file, indent=4) 

        
    elif opcion == '2':
        print("Ha seleccionado la opcion 2.")
        print("".center(50,"-"))

        while True:
            tipo = input(f"Ingrese el tipo de la gema (Onepiece, Hache, Callisto, Backaid, Kaminari): ").capitalize()
            if tipo=="Onepiece" or tipo=="Hache" or tipo=="Callisto" or tipo=="Backaid" or tipo=="Kaminari":
                break
            else:
                print("\nTipo de gema no valida.\n")
                    
        
        while True:
            try:
                poder = int(input(f"Ingrese el poder de la gema: "))
                if poder >=0:
                    break
                else:
                   print("\nNo puede ser un numero negativo.\n") 
            except:
                print("\nEl poder debe ser un numero entero mayor o igual a 0.\n")

        while True:
            tipoarma = input("Tipo de arma valida para la gema (Cuchillos, Lanzas, Martillos, Espadas): ").capitalize()
            if tipoarma=="Cuchillos" or tipoarma=="Lanzas" or tipoarma=="Martillos" or tipoarma=="Espadas":
                break
            else:
                print("\nTipo de arma no valida.\n")



        dir =  f"{dir_act}/bd/gemas"
        filename = "gemasinfo.json"
        if os.path.exists(f"{dir}/{filename}"):
            with open(f"{dir}/{filename}","r") as j:
                data = json.load(j)
            
            #Recorre la data, si encuentra una gema que ya esté creado, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data["gemas"])):
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

        while True:
            tipo = input(f"Ingrese el tipo de arma (Cuchillos, Lanzas, Martillos, Espadas): ").capitalize()
            if tipo=="Cuchillos" or tipo=="Lanzas" or tipo=="Martillos" or tipo=="Espadas":
                break
            else:
                print("\nTipo de arma no valida.\n")
        
        nombre = input(f"Ingrese el nombre del arma: ").capitalize()
        while True:
            try:
                poder = int(input(f"Ingrese el poder del arma: "))
                posicion = int(input(f"Posicion en la que el arma debe ser usada: "))
                if poder>=0 and posicion>=0:
                    print("Arma creada con exito.")
                    break
                else:
                    print("\nPoder o Posicion no pueden ser numeros negativos.\n")
            except:
                print("\nEl poder y la posicion deben ser numeros enteros mayores o iguales a 0. \n")
        
        dir =  f"{dir_act}/bd/arma"
        filename = "armasinfo.json"
        if os.path.exists(f"{dir}/{filename}"):
            with open(f"{dir}/{filename}","r") as j:
                data = json.load(j)

            #Recorre la data, si encuentra un arma que ya esté creada, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data["armas"])):
                if data["armas"][i]["nombre"]==nombre:
                    del data["armas"][i]
                    break
                else:
                    pass

            data['armas'].append({
            'tipo': tipo,
            'nombre': nombre,
            'poder': int(poder),
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
            'poder': int(poder),
            'posicion': int(posicion) 
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
            for i in range(len(data[f'{tipo}'])):
                if data[f'{tipo}'][i]["nombre"]==nombre:
                    del data[f'{tipo}'][i]
                    break
                else:
                    pass

            data[f'{tipo}'].append({
            'nombre': nombre,
            'poder': int(poder),
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
            'poder': int(poder),
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
        while True:
            nombre = input(f"Ingrese el nombre de la dinastía (swift, flutter, java): ").capitalize()
            if nombre=="Swift" or nombre=="Flutter" or nombre=="Java":
                break
            else:
                print("\nDinastia no valida.\n")
        
        
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
            for i in range(len(data["dinastias"])):
                if data["dinastias"][i]["nombre"]==nombre:
                    del data["dinastias"][i]
                    break
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
                if pos>=0:
                    print("".center(50,"-"))
                    while True:
                        try:
                            pod = int(input(f"Ingrese la suma del poder de la posicion {pos}: "))
                            if pod:
                                print("Posicion creada")
                                break
                        except:
                            print("\nLa suma del poder debe ser un numero entero.\n")
                    print("".center(50,"-"))
                    break
                else:
                    print("\nPosicion no puede ser numero negativo.\n")
            except:
                print("\nLa posicion debe ser un numero entero.\n")
                
        dir =  f"{dir_act}/bd/arma"
        filename = "positioninfo.json"
        if os.path.exists(f"{dir_act}/bd/arma/{filename}"):
            with open(f"{dir_act}/bd/arma/{filename}","r") as j:
                data = json.load(j)

            #Recorre la data, si encuentra una posición que ya esté creada, la elimina y la vuelve a crear para no duplicar el registro
            for i in range(len(data['posiciones'])):
                if data['posiciones'][i]['posicion']==pos:
                    del data['posiciones'][i]
                    break
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
        # Se crea un directorio donde se guardará la mejor combinación
        combinacion = {}
        combinacion["mejorcombinacion"] = []

        #Abre el json donde está la info de las gemas
        dir =  f"{dir_act}/bd/gemas"
        filename = "gemasinfo.json"
        with open(f"{dir}/{filename}","r") as j:
            datagemas = json.load(j)

        for i in range(len(datagemas["gemas"])):
            gema = datagemas["gemas"][i]["tipo"]
            podgema = datagemas["gemas"][i]["poder"]
                
            #Abre el json donde está la info de las armas
            dir =  f"{dir_act}/bd/arma"
            filename = "armasinfo.json"
            with open(f"{dir}/{filename}","r") as j:
                dataarmas = json.load(j)
            
            # Se iteran las armas
            for i in range(len(dataarmas["armas"])):
                arma = dataarmas["armas"][i]["nombre"]
                podarma = dataarmas["armas"][i]["poder"]
                
                #Abre el json donde está la info de las posiciones
                dir =  f"{dir_act}/bd/arma"
                filename = "positioninfo.json"
                with open(f"{dir}/{filename}","r") as j:
                    datapos = json.load(j)
                
                # Se iteran las posiciones
                for i in range(len(datapos["posiciones"])):
                    ubicacion = datapos["posiciones"][i]["posicion"]
                    podpos = datapos["posiciones"][i]["poder"]

                    #Abre el json donde está la info de las dinastias
                    dir =  f"{dir_act}/bd/arma"
                    filename = "dinastiasinfo.json"
                    with open(f"{dir}/{filename}","r") as j:
                        datadinas = json.load(j)

                    # Se iteran las dinastias
                    for i in range(len(datadinas["dinastias"])):
                        dinastia = datadinas["dinastias"][i]["nombre"]

                        # Como las dinastias pueden tener varias posiciones entonces se itera la lista de posicion-poder
                        for poder in datadinas["dinastias"][i]["poder"]:
                            poddinas = poder[1]
                            
                            sumapoder = (podarma+podpos+podgema+poddinas)

                            if combinacion["mejorcombinacion"]:
                                for i in range(len(combinacion["mejorcombinacion"])):
                                    # Recorre el diccionario combinacion, accede a su llave valor
                                    for llave,valor in combinacion["mejorcombinacion"][i].items():
                                        # Si la suma de los poderes de esta iteración es mayor a la que ya está registrada entonces lo borra y crea uno nuevo
                                        if sumapoder>valor:
                                            del combinacion["mejorcombinacion"][i]

                                            combinacion["mejorcombinacion"].append({
                                                f"{arma},{str(ubicacion)},{gema},{dinastia}": sumapoder
                                                })
                                            break                             
                            else:
                                combinacion["mejorcombinacion"].append({
                                f"{arma},{str(ubicacion)},{gema},{dinastia}": sumapoder
                                })
        
        for i in range(len(combinacion["mejorcombinacion"])):
            for llave,valor in combinacion["mejorcombinacion"][i].items():
                print("La combinación con el mayor poder es: \n")
                print(f"'{llave}' con un poder de {valor}" )

    elif opcion == '7':
        print("\n")
        print("Programa Finalizado".center(50,"-"))
        print("Programa Finalizado".center(50,"-"))
        print("Programa Finalizado".center(50,"-"))
        print("\n")
        break
    else:
        print("Entrada no valida, digite un numero del menú")
