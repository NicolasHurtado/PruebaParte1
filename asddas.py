""" import json
import os

dir_act = os.path.abspath(os.path.dirname(__file__))

with open(f"{dir_act}/bd/gemas/gemaid/gemasinfo.json","r") as j:
    data = json.load(j)

if data['gemas'][1]['tipo']=="Haryux":
    print(data['gemas'][1]['poder'])
else:
    print("No lo encontré")  """

lista = []

x = int(input("Posicion: "))
y = int(input("Suma de poder en esa posicion:"))

tru = (x,y)
lista.append(tru)

print(lista)