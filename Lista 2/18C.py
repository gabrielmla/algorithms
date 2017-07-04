n = input()
stripe = map(int, raw_input().split())
total = 0
leftSum = 0
div = 0

for i in range(n):
	total += stripe[i]
	
for i in range(n-1):
	leftSum += stripe[i]
	if leftSum * 2 == total:
		div += 1

print div

