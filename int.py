import sys
from Tkinter import *
from math import * 
import numpy as np
from sympy import *

etapa = int(raw_input("Ingresa el numero de etapas: "))
puntoEvaluar = float(raw_input("Ingresa tu punto a evaludar"))

matriz = [0.0]*etapa
vector= [0.0]*etapa

for i in range(etapa):
	matriz[i] = [0.0]*etapa

for i in range(etapa):
	x = raw_input("Ingresa x: ")
	fx = raw_input("Ingresa fx: ")
	vector[i] = float(x)
	matriz[i][0] = float(fx)


print vector
print matriz


for i in range(1,etapa):
	for j in range(i,etapa):
		matriz[j][i] = ((matriz[j][i-1] - matriz[j-1][i-1]) / (vector[j]-vector[j-i]))

#IMPRIME
for i in range(etapa):
	for j in range(etapa):
		print matriz[i][j] 

final = 0
almacen = 1.0
for i in range(etapa):
	almacen = matriz[i][i]
	for j in range(1,i+1):
		almacen= almacen * (puntoEvaluar - vector[j-1])
	#print final
	final = final + almacen
print final