def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
gcd_ab = gcd(a,b)
print(a*b//gcd_ab)