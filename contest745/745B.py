def checa_buraco(ma):
	for i in xrange(len(ma)):
		for j in xrange(1, len(ma[i])-1):
			if ma[i][j] == '.' and ma[i][j-1] == 'X' and ma[i][j+1] == 'X':
				return False
	return True

def put_right(ma):
	aux = ma
	for i in xrange(len(ma)):
		aux[i] += ma[i]
	return aux
	
n, m = map(int, raw_input().split())
r = []
l = []
u = []
d = []
for i in xrange(n):
	ent = raw_input()
	r.append(ent)
	l.append(ent)
	u.append(ent)
	d.append(ent)
	
put_right(r)
if checa_buraco(r):
	print "YES"
elif checa_buraco(l):
	print "YES"
elif checa_buraco(u):
	print "YES"
elif checa_buraco(d):
	print "YES"
else:
	print "NO"
	
print r, l, u , d

