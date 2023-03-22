from math import gcd

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a = a1*b2 + a2*b1
b = b1*b2
g = gcd(a,b)
print(a//g, b//g)