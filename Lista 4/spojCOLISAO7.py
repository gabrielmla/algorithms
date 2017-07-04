# Primeiro Retangulo
a0, b0, a1, b1 = map(int, raw_input().split())
# Segundo Retangulo
x0, y0, x1, y1 = map(int, raw_input().split())

if a1 < x0: print 0
elif x1 < a0: print 0
elif b1 < y0: print 0
elif y1 < b0: print 0
else: print 1
