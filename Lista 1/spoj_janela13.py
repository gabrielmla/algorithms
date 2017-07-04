coordenadas = map(int, raw_input().split())
coordenadas.sort()

base = 600
 
base -= 200
if coordenadas[1] > coordenadas[0] + 199:
	base -= 200
else:
	base -= coordenadas[1] - coordenadas[0]
 
if coordenadas[2] > coordenadas[1] + 199:
	base -= 200
else:
	base -= coordenadas[2] - coordenadas[1]
 
print base * 100
 
