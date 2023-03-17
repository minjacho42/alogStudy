import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

houses, cuisines = [], []

for i in range(N):
    for j, c in enumerate(list(map(int, input().split()))):
        if c == 1:
            houses.append((i,j))
        elif c == 2:
            cuisines.append((i,j))

def length(dot1, dot2):
    return abs(dot1[0] - dot2[0]) + abs(dot1[1] - dot2[1])

lengths = []

for house in houses:
    lengths.append(tuple(map(lambda x: length(x, house), cuisines)))

answer = 0

for combination in combinations(range(len(cuisines)), M):
    new_length = sum(map(lambda x: min([x[idx] for idx in combination]), lengths))
    if answer == 0:
        answer = new_length
    else:
        answer = min(new_length, answer)

print(answer)