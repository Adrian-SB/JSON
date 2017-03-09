# -*- coding: utf-8 -*-

import json

raiz = json.loads(open('Asociaciones.json').read())

#4-Solicita el nombre de una asociación, muestra el fundador, el número de teléfono y el correo.

asosiaciones=raiz["items"]

nomAso=raw_input("Dime una asociación:")

for a in asosiaciones:
    if nomAso == a:
        fundador=raiz["items"][a]["author"]
        telefono=raiz["items"][a]["elements"]["a540758e-50f7-4e15-93eb-26548094bc43"]["data"]["0"]["value"]
        correo=raiz["items"][a]["elements"]["06974ac5-d947-4817-9bce-c5449f0377ad"]["data"]["0"]["value"]
        print "\nFundador:",fundador
        print "Teléfono:",telefono
        print "E-mail:",correo