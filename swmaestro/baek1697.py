import sys
from collections import deque

input = sys.stdin.readline

N, K = tuple(map(int, input().split()))

def bfs(n, k):
    visited = set()
    que = deque()
    count = 0
    que.appendleft((n,count))
    while n != k:
        n, count = que.pop()
        if n-1 not in visited and 0<=n-1<=100000:
            que.appendleft((n-1, count+1))
            visited.add(n-1)
        if n+1 not in visited and 0<=n+1<=100000:
            que.appendleft((n+1, count+1))
            visited.add(n+1)
        if 2*n not in visited and 0<=2*n<=100000:
            que.appendleft((2*n, count+1))
            visited.add(2*n)
    return count

print(bfs(N,K))
