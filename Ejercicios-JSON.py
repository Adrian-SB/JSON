# -*- coding: utf-8 -*-

import json

raiz = json.loads(open('Asociaciones.json').read())

#1-Lista las distintas categorías que pueden poseer las asociaciones.

categorias=raiz["categories"]

guion=['-']

for c in categorias:
    for g in guion:#Limpiador
            c=c.replace(g," ")
    print c.title()

#2-Solicita una categoría y muestra el número de empresas que pertenecen a dicha categoría.

contar=raw_input("Dime una categoría:")

asosiaciones=raiz["items"]

print asosiaciones

for a in asosiaciones:
    categoria2=raiz["items"][a]["categories"]
    for c2 in categoria2:
        if c2 == contar:
            print "Bien"
                #print c.count(contar)
