n, d = map(int, raw_input().split())
ship = 0
friends = []

for i in xrange(n):
	friends.append(map(int, raw_input().split()))

sFriends = sorted(friends, key = lambda x: x[0])
ssFriends = sorted(friends, key = lambda x: x[1], reverse = True)

i = 0
j = n - 1
while i < j:
	if abs(sFriends[i][0] - sFriends[j][0]) <= d:
		ship += sFriends[i][1] + sFriends[j][1]
		i += 1
		j -= 1
	j -= 1
	if i == j:
		ship += sFriends[i][1]
if ssFriends[0][1] > ship:
	ship = ssFriends[0][1]
print ship
