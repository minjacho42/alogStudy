from collections import defaultdict
from math import sqrt

primes = defaultdict(lambda :True)

primes[1] = False

t = int(input())
nums = [int(input()) for __ in range(t)]

n = 1000000
for i in range(2, int(sqrt(2*n)) + 1):
        if primes[i]:
            for j in range(2*i, 2*n+1, i):
                primes[j] = False


for n in nums:
    answer = 0
    for i in range(1, n//2 + 1):
        if primes[i] and primes[n - i]:
            answer += 1
    print(answer)
    