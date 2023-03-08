import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

row = defaultdict(list)
column = defaultdict(list)

for i in range(N):
    for j, c in enumerate(list(input().strip())):
        if c == 'X':
            row[i].append(j)
            column[j].append(i)

def solution(row, column, n):
    answers = []
    for line in [row, column]:
        answer = 0
        for i in range(n):
            start = -1
            for num in line[i]+[n]:
                if num - start > 2:
                    answer += 1
                start = num
        answers.append(answer)
    return answers

answers = solution(row,column,N)
print(answers[0], answers[1])
        