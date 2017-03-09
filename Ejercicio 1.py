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
print ""