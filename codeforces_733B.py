nCol = input()
cols = []
for i in xrange(nCol):
	cols.append(map(int, raw_input().split()))

preMaxBeauty = 0
leftTotal = 0
rightTotal = 0
maxBeauty = 0
colBeauty = 0
posMaxBeauty = 0
for c in xrange(nCol):
	leftTotal += cols[c][0]
	rightTotal += cols[c][1]
	beauty = abs(cols[c][0] - cols[c][1])
	if beauty > maxBeauty:
		maxBeauty = beauty
		colBeauty = c
	
preMaxBeauty = abs(leftTotal - rightTotal)

leftTotal -= cols[colBeauty][0]
rightTotal -= cols[colBeauty][1]
temp = cols[colBeauty][0]
cols[colBeauty][0] = cols[colBeauty][1]
cols[colBeauty][1] = temp
leftTotal += cols[colBeauty][0]
rightTotal += cols[colBeauty][1]
posMaxBeauty = abs(leftTotal - rightTotal)

if preMaxBeauty > posMaxBeauty:
	print 0
else:
	print colBeauty + 1





