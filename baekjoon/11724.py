import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1-1][n2-1], graph[n2-1][n1-1] = 1, 1

def solution(graph):
    n = len(graph)
    visit = set()
    answer = 0
    for i in range(n):
        if i not in visit:
            visit.add(i)
            answer += 1
            que = deque()
            que.appendleft(i)
            while len(que) > 0:
                node = que.pop()
                for j in range(n):
                    if graph[node][j] == 1 and j not in visit:
                        que.appendleft(j)
                        visit.add(j)
    return answer

print(solution(graph))