import json
import os

dir_act = os.path.abspath(os.path.dirname(__file__))

with open(f"{dir_act}/bd/gemas/gemaid/gemasinfo.json","r") as j:
    data = json.load(j)

if data['gemas'][1]['tipo']=="Haryux":
    print(data['gemas'][1]['poder'])
else:
    print("No lo encontré") 
