n = input()
md = n

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

if n % 2 == 0:
	md = 2
elif sum_digits(n) % 3 == 0:
	md = 3
elif str(n)[-1] == '0' or str(n)[-1] == '5':
	md = 5

maiorD = n / md

print maiorD
