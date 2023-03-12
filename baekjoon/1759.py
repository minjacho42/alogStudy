import sys
from itertools import combinations as comb

input = sys.stdin.readline

l, c = map(int, input().split())
alpha = set(input().split())

def solution(l, alpha):
    answers = []
    alphaList = sorted(list(alpha))
    mo = sorted(list(alpha&set(['a','e','i','o','u'])))
    ja = sorted(list(alpha-set(['a','e','i','o','u'])))
    for j in range(2, l):
        m = l - j
        if m > len(mo) or j > len(ja):
            continue
        combMo = list(comb(mo,m))
        combJa = list(comb(ja,j))
        for cm in combMo:
            for cj in combJa:
                answers.append(''.join(sorted(cm+cj)))
    return sorted(answers)

for str in solution(l,alpha):
    print(str)


        