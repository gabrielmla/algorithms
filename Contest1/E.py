n = input()
pres = {}
for i in xrange(n):
	e = raw_input().split()
	pres[e[0]] = e[1:]
while True:
	try:
		f = raw_input().split()
		if pres.has_key(f[0]):
			if f[1] in pres[f[0]]:
				print "Uhul! Seu amigo secreto vai adorar o/"
			else:
				print "Tente Novamente!"
		else:
			print "Tente Novamente!"
	except:
		break
