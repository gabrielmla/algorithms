shovel, r = map(int, raw_input().split())
total = shovel
min = 1

while total % 10 != 0 and total % 10 != r:
	total += shovel
	min += 1


if min >= 10:
	print 10
else:
	print min
