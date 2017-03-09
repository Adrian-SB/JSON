# -*- coding: utf-8 -*-

import json

raiz = json.loads(open('Asociaciones.json').read())

#5-Solicita una categoría y muestra las asociaciones pertenecientes a dicha categoría.

asosiaciones=raiz["items"]

guion=['-']

nomAsoCat=raw_input("Dime una categoria:")

print "\nLas siguientes asosiaciones pertenecen a la categoria",nomAsoCat
print "------------------------------------------------------------------"

for a in asosiaciones:
    categoria3=raiz["items"][a]["categories"]
    for x, c in categoria3.items():
        if nomAsoCat == c:
            for g in guion:#Limpiador
                a=a.replace(g," ")
                print a.title()