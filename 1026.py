def final(a,b,c,d):
	if a == 0 and b == 0 and c == 0 and d == 0:
		return True
	return False
	
while True:
	h1, m1, h2, m2 = map(int, raw_input().split())
	minutos = 0
	
	if final(h1, m1, h2, m2):
		break
		
	while h1 % 24 != h2:
		h1 += 1
		minutos += 60
	print minutos
			
