import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1 - 1][node2 - 1] = 1
    graph[node2 - 1][node1 - 1] = 1

def solution(graph):
    visit = set([0])
    que = deque()
    for i in range(N):
        if graph[0][i] == 1:
            que.appendleft(i)
            visit.add(i)
    while len(que) > 0:
        node = que.pop()
        for i in range(N):
            if graph[node][i] == 1 and i not in visit:
                que.appendleft(i)
                visit.add(i)
    return len(visit) - 1

print(solution(graph))