N, M = map(int, input().split())

graph = [list(map(int, input().split())) for __ in range(N)]

def polyMax(graph, i, j):
    n, m = len(graph), len(graph[0])
    polyomino = [[(0,1), (0,2), (0,3)], [(1,0),(2,0),(3,0)], [(0,1),(1,0),(1,1)],
             [(1,0),(2,0),(2,1)], [(1,0),(2,0),(2,-1)], [(1,0), (2,0), (0,1)], [(1,0), (2,0), (0,-1)],
             [(0,1), (0,2), (1,0)], [(0,1), (0,2), (-1, 0)], [(0,1), (0,2), (1,2)], [(0,1), (0,2), (-1,2)],
             [(1,0), (1,1), (2,1)], [(1,0), (1,-1), (2,-1)], [(0,1), (1,1), (1,2)], [(0,1), (-1,1), (-1,2)],
             [(0,-1), (0,1), (1,0)], [(0,-1), (0,1), (-1,0)], [(-1,0), (1,0), (0,1)], [(-1,0),(1,0),(0,-1)]]
    maxSum = graph[i][j]
    for directions in polyomino:
        s = graph[i][j]
        for d in directions:
            new_i, new_j = i + d[0], j + d[1]
            if not (0<=new_i<n and 0<=new_j<m):
                break
            s += graph[new_i][new_j]
        else:
            if maxSum < s:
                maxSum = s
    return maxSum
answer = 0
for i in range(N):
    for j in range(M):
        newAnswer = polyMax(graph, i, j)
        answer = newAnswer if newAnswer > answer else answer

print(answer)