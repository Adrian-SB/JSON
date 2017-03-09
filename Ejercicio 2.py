# -*- coding: utf-8 -*-

import json

raiz = json.loads(open('Asociaciones.json').read())

#2-Solicita una categoría y muestra el número de empresas que pertenecen a dicha categoría.

buscar=raw_input("Dime una categoría:") # Nombre categoría sin limpiador// De Vecinos = de-vecinos

asosiaciones=raiz["items"]

for a in asosiaciones:
    categoria2=raiz["items"][a]["categories"]
    for x, c in categoria2.items():
        if buscar == c:
            cont=len(c)

print""
print "Hay",cont,"asosiaciones pertenecientes a la categoría",buscar
