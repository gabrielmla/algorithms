name = raw_input()

alphabet = "abcdefghijklmnopqrstuvwxyz"
pointer = 0
pos_counter = 0

for l in name:
	l_pos = alphabet.index(l)
	dist = abs(pointer - l_pos)
	minimo = min(dist, 26 - dist)
	pos_counter += minimo
	pointer = l_pos

print pos_counter
	
