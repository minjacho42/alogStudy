import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j, n in enumerate(input().strip()):
        graph[i][j] = int(n)

answers = []

def bfs(start):
    sum = 0
    que = deque()
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    que.append(start)
    graph[start[0]][start[1]] = 0
    while len(que) > 0:
        node = que.popleft()
        sum += 1
        for direction in directions:
            i, j = node[0]+direction[0], node[1]+direction[1]
            if 0<=i<N and 0<=j<N and graph[i][j] == 1:
                que.append((i,j))
                graph[i][j] = 0
    return sum

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answers.append(bfs((i,j)))
print(len(answers))
for answer in sorted(answers):
    print(answer)