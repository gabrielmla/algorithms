n = input()
w = map(int, raw_input().split())
maior = sorted(w)[-1]
total = 0
for i in w:
	if i < maior:
		total += maior - i

print total
