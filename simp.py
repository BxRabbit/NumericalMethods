import sys

puntos = int(raw_input("Cuantos puntos quieres? "))
vector = [0.0]*puntos


for i in range(0,puntos):
	vector[i] = float(raw_input("Ingresa el punto: "))
print vector

if (puntos-1)%2==0:
	a = float(raw_input("Ingresa a: "))
	b = float(raw_input("Ingresa b: "))
	h = ((b - a)/(puntos - 1))
	resultado = 0

	for i in range(0,puntos-1,2):
		resultado = resultado + (h/3) * (vector[i] + (4 * vector[i+1]) + (vector[i+2]))
	print resultado

elif (puntos-1)%3==0:
	a = float(raw_input("Ingresa a: "))
	b = float(raw_input("Ingresa b: "))
	h = ((b - a)/(puntos - 1))
	resultado = 0

	for i in range(0,puntos-1,3):
		resultado = resultado + ((3*h)/8) * (vector[i] + (3*vector[i+1]) + (3*vector[i+2])+(vector[i+3]))
	print resultado
else:
	a = float(raw_input("Ingresa a: "))
	b = float(raw_input("Ingresa b: "))
	h = ((b - a)/(puntos - 1))
	resultado = 0
	ab = a + (3*h)
	htercio = ((b-ab)/(puntos-4))
	hoctavos = ((ab - a)/3)

	resultado = ((3*hoctavos)/8)*(vector[0] + (3 * vector[1]) + (3 * vector[2]) + (vector[3]))

	for i in range(4,puntos-1,2):
		resultado = resultado + (h / 3) * (vector[i-1] + (4 * vector[i]) + (vector[i + 1]))
	print resultado

