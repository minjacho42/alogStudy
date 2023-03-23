from collections import defaultdict
from math import sqrt

primes = defaultdict(lambda :True)

primes[1] = False

while True:
    answer = 0
    n = int(input())
    if n == 0:
        break
    for i in range(2, int(sqrt(2*n)) + 1):
        if primes[i]:
            for j in range(2*i, 2*n+1, i):
                primes[j] = False
    for i in range(n+1, 2*n+1):
        if primes[i]:
            answer += 1
    print(answer)
