a, b = map(int, raw_input().split())
steps = [b]

while b > a:
	sB = str(b)
	if int(sB[-1]) == 1:
		b = (b - 1)/ 10
		steps.append(b)
	elif int(sB[-1]) % 2 == 0:
		b = (b/2)
		steps.append(b)
	else:
		break

if b == a:
	print "YES"
	print len(steps)
	for i in reversed(steps):
		print i,
else:
	print "NO"
