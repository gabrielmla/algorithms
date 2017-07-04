nCol = input()
cols = []
for i in xrange(nCol):
	cols.append(map(int, raw_input().split()))
	
leftTotal = 0
rightTotal = 0

for c in xrange(nCol):
	leftTotal += cols[c][0]
	rightTotal += cols[c][1]

maxBeauty = abs(leftTotal - rightTotal)
maxBeautyIndex = 0

for i in xrange(nCol):
	beauty = abs((leftTotal - cols[i][0] + cols[i][1]) - (rightTotal - cols[i][1] + cols[i][0]))
	if beauty > maxBeauty:
		maxBeauty = beauty
		maxBeautyIndex = i + 1

print maxBeautyIndex
