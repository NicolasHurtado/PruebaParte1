import json
import os

dir_act = os.path.abspath(os.path.dirname(__file__))

""" with open(f"{dir_act}/bd/gemas/gemaid/gemasinfo.json","r") as j:
    data = json.load(j)

if data['gemas'][1]['tipo']=="Haryux":
    print(data['gemas'][1]['poder'])
else:
    print("No lo encontré")  """

dir =  f"{dir_act}/bd/people"
filename = "soldadosinfo.json"

if os.path.exists(f"{dir}/{filename}"):
    with open(f"{dir}/{filename}","r") as j:
        data = json.load(j)

print(data["soldados"])


""" for i in range(len(data)+1):
    if data["soldados"][i]["apodo"]=="JHOJAN":
        del data["soldados"][i]
        data['soldados'].append({
            'apodo': "JHOJAN",
            'poseegemas': False,
            'gemas': [],
            'tipoarma': "Espadas",
            'armas': ["Samurai","Katana"],
            'ubicacion': 58,
            'dinastia': "java" 
            })
        with open(os.path.join(dir,filename), 'w') as file:
            json.dump(data, file, indent=4)
        break
    else:
        pass  """

print("------------------------------------------")


