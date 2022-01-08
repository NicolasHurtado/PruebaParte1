import json
import os

dir_act = os.path.abspath(os.path.dirname(__file__))

dir =  f"{dir_act}/bd/people"
filename = "soldadosinfo.json"
if os.path.exists(f"{dir_act}/bd/arma/{filename}"):
    with open(f"{dir_act}/bd/arma/{filename}","r") as j:
        data = json.load(j)

""" "apodo": "BUNAK",
    "poseegemas": true,
    "gemas": [
        "Hache",
        "Backaid"
    ],
    "tipoarma": "Lanzas",
    "armas": [
        "Arco",
        "Arco 2.0"
    ],
    "ubicacion": 21,
    "dinastia": "Flutter"
 """
poseegemas = False
armas= ["Arco","Arco 2.0"]
gemas= ["Onepiece","Backaid"]
ubicacion = 7
dinastia = "Java"


combinaciones = {}
combinaciones["combinaciones"] = []


if poseegemas == True:
    #Recorre el arreglo de gemas
    for gema in gemas:
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
        
        print(f"Poder gema: {podgema}")
        #Recorre el arreglo de armas
        for arma in armas:
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
            
            print(f"Poder arma: {podarma}")
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
                            f"{arma},{str(ubicacion)},{gema},{dinastia}":(podarma+podpos+podgema+poddinas)
                        })   
                else:
                    pass       
else:
    #Recorre el arreglo de armas
    podgema = 0
    for arma in armas:
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
        
        print(f"Poder arma: {podarma}")
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


for i in range(len(combinaciones["combinaciones"])):
    for llave,valor in combinaciones["combinaciones"][i].items():
        print(f"{llave} : {valor}" )



""" 
#Abre el json donde está la info de las dinastias
dir =  f"{dir_act}/bd/arma"
filename = "dinastiasinfo.json"
with open(f"{dir}/{filename}","r") as j:
    datadinas = json.load(j)

for i in range(len(datadinas["dinastias"])):
    if datadinas["dinastias"][i]["nombre"]==dinastia:
        for poder in datadinas["dinastias"][i]["poder"]:
            poddinas = poder[1]
        break
    else:
        pass  """











