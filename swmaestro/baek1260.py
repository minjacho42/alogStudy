from collections import deque

def BFS(graph, V):
    visited = []
    que = deque()
    que.appendleft(V)
    visited.append(V)
    while len(que) > 0:
        node = que.pop()
        for i, connected in enumerate(graph[node - 1]):
            if connected and i+1 not in visited:
                que.appendleft(i+1)
                visited.append(i+1)
    string = ' '.join(list(map(str,visited)))
    return string.strip()


def DFS(graph, V):
    visited = []
    visited.append(V)
    def dfs(start):
        for i, connected in enumerate(graph[start-1]):
            if i+1 not in visited and connected:
                visited.append(i+1)
                dfs(i+1)
    dfs(V)
    string = ' '.join(list(map(str,visited)))
    return string.strip()


if __name__ == '__main__':
    N, M, V = tuple(map(int, input().split()))
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        n1, n2 = tuple(map(int, input().split()))
        graph[n1-1][n2-1], graph[n2-1][n1-1] = (1, 1)
    print(DFS(graph, V))
    print(BFS(graph, V))