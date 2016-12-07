#! /usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *
import math


fx= raw_input("Ingresa la funcion donde se evaluara x: ")
vi = raw_input("Ingresa el valor inicial: ")
ep = float(raw_input("Ingresa el error estimado: "))
maxiter = int(raw_input("ingrese maximo de iteraciones: "))

fx = fx.replace("x","y")
xi = float(vi)
dfx = diff(fx)
dfx = str(dfx)
	

for i in range(maxiter):
	
	fxi = fx.replace("exp", "math.exp")
	fxi = eval(fxi.replace("y", str(xi)))
	dfxi = dfx.replace("exp", "math.exp")
	dfxi = eval(dfxi.replace("y", str(xi)))

	resultado = xi - (float(fxi)/float(dfxi))
	print "xi+1 = %f No. iteracion: %i" % (resultado, i)
	
	errorP = ((resultado - xi) / resultado) * 100
	errorP = abs(errorP)
	print "error = %f" % errorP
	
	xi = float(resultado)
	if(errorP < ep):
		break


print "La aproximacion a la raiz es: %f" % xi
print "Con un error estimado de: %f" % errorP