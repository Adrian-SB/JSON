# -*- coding: utf-8 -*-

import json

raiz = json.loads(open('Asociaciones.json').read())

#3-Teclea un año entre el 2013 y el 2014 y muestra las asociaciones que han sido creadas en ese año.

guion=['-']

asosiaciones=raiz["items"]

anyo=raw_input("Dime un año entre 2013-2014:")

for a in asosiaciones:
    creacion=raiz["items"][a]["created"]
    for g in guion:#Limpiador
            a=a.replace(g," ")
    if anyo in creacion:
        print "\nLa asociación",a.title(),"fue creada el",creacion.split(" ")[0]