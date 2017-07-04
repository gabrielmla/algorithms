n = input()
a = map(int, raw_input().split())
b = []
bFlag = False

for i in range(n-1):
	if b[i] > b[i+1] and not bFlag:
		bFlag = True
		b.append(i)
	if bFlag:
		if b[i] > b[i+1]:
			bFlag = False
			b.append(i)
			
if len(b) == 0:
    print "yes\n1 1"
elif len(b) == 1 and b[0] == 0:
	b.append(n-1)
    print "yes\n%d %d" % (b[0] + 1, b[1] + 1)
elif len(b) > 2:
    print "no"
else:
    auxF = False
	
	if len(b) == 1:
		b.append(n-1)
		
    aux = a[b[0]]
    a[b[0]] = a[b[1]]
    a[b[1]] = aux
	
    for j in range(b[0]):
        if a[j] > a[j+1]:
            auxF = True
            break
    for j in range(b[1], n-1, 1):
        if a[j] > a[j+1]:
            auxF = True
            break
    if auxF:
        print "no"
    else:
        print "yes\n%d %d" % (b[0] + 1, b[1] + 1)

