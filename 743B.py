n, k = map(int, raw_input().split())
res = 0

# posicoes impar sao sempre 1, entao olhar as pares
while k % 2 == 0:
	k = k/2
	res += 1

print res + 1
