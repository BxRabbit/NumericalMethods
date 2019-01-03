#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math
from decimal import *
from sympy import *


fx = raw_input("Ingresa la funcion donde se evaluara X: ")
xi = Decimal(raw_input("Ingresa el valor incial de xi: "))
ximenosuno = Decimal(raw_input("Ingresa el valor inicial xi-1: "))
ep = float(raw_input("Ingresa el error porcentual: "))
maxiter = int(raw_input("Ingresa el numero maximo de iteraciones: "))

fx = fx.replace("x","y")

for i in range(maxiter):
	
	fx = fx.replace("exp", "math.exp")			
	fxi = eval(fx.replace("y", str(xi)))
	fximenosuno = eval(fx.replace("y", str(ximenosuno)))
	
	resultado = xi - ((fxi * (ximenosuno - xi)) / (fximenosuno-fxi))
	
	ValorAnterior = 0 
	ValorActual = resultado
	
	errorP = ((ValorActual - ValorAnterior)/ValorActual)*100

	xi = resultado
	ximenosuno = fximenosuno
	ValorAnterior= resultado

	if(errorP < ep):
			break

print "El resultado es: %f" % resultado
print "Con un error de: %f" % errorP

				









