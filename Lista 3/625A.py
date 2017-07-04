n = long(raw_input())
a = long(raw_input())
b = long(raw_input())
c = long(raw_input())
buy = 0
if n >= b:
	if a >= (b-c):
		g = (n-c)/(b-c)
		n -= g*(b-c)
		buy = g

print buy + (n/a)
