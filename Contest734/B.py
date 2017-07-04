k2, k3, k5, k6 = map(int, raw_input().split())

total = 0

n = min(k2,k5,k6)
k2 -= n
k5 -= n
k6 -= n

m = min(k2,k3)

total += 256*n
total += 32*m

print total
	
