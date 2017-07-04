s = raw_input()
newS = " " + s + " "
gPos = 0
maxJump = 0

vowels = "AEIOUY "

while gPos != len(newS) - 1:
	jump = 0
	while True:
		gPos += 1
		jump += 1
		if newS[gPos] in vowels:
			break
	if jump > maxJump:
		maxJump = jump

print maxJump
