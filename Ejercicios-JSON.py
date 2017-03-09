# -*- coding: utf-8 -*-

import json

raiz = json.loads(open('Asociaciones.json').read())

print "1-Lista las distintas categorías que pueden poseer las asociaciones.\n"

categorias=raiz["categories"]

guion=['-']

for c in categorias:
    #for g in guion:#Limpiador
            #c=c.replace(g," ")
    print c#.title()
print ""

print "2-Solicita una categoría y muestra el número de empresas que pertenecen a dicha categoría.\n"

buscar=raw_input("Dime una categoría:") # Nombre categoría sin limpiador// De Vecinos = de-vecinos

asosiaciones=raiz["items"]


for a in asosiaciones:
    categoria2=raiz["items"][a]["categories"]
    for x, c in categoria2.items():
        if buscar == c:
            cont=len(c)

print""
print "Hay",cont,"asosiaciones pertenecientes a la categoría",buscar


print "\n3-Teclea un año entre el 2013 y el 2014 y muestra las asociaciones que han sido creadas en ese año.\n"


anyo=raw_input("Dime un año entre 2013-2014:")

print ""

for a in asosiaciones:
    creacion=raiz["items"][a]["created"]
    #for g in guion:#Limpiador
            #a=a.replace(g," ")
    if anyo in creacion:
        print "La asociación",a,"fue creada el",creacion.split(" ")[0]


print "\n4-Solicita el nombre de una asociación, muestra el fundador, el número de teléfono y el correo.\n"


nomAso=raw_input("Dime una asociación:")

for a in asosiaciones:
    if nomAso == a:
        fundador=raiz["items"][a]["author"]
        telefono=raiz["items"][a]["elements"]["a540758e-50f7-4e15-93eb-26548094bc43"]["data"]["0"]["value"]
        correo=raiz["items"][a]["elements"]["06974ac5-d947-4817-9bce-c5449f0377ad"]["data"]["0"]["value"]
        print "\nFundador:",fundador
        print "Teléfono:",telefono
        print "E-mail:",correo

print "5-Solicita una categoría y muestra las asociaciones pertenecientes a dicha categoría.\n"

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

