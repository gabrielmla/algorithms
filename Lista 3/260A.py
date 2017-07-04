a, b, n = map(int, raw_input().split())
flag = False
a *= 10
for i in range(10):
	if (a + i) % b == 0:
		a += i
		n -= 1
		flag = True
		break

a = str(a)
a += "0" * n

if flag:
	print a
else:
	print -1