from collections import deque

directions = [(0,1), (1,0), (0,-1), (-1,0)]
M, N = map(int, input().split())
unrotten = set()
none = set()
que = deque()

for i in range(N):
    for j, c in enumerate(list(map(int, input().split()))):
        if c == 0:
            unrotten.add((i,j))
        elif c == 1:
            que.appendleft((i, j, 0))
time = 0
while len(que) > 0:
    x, y, t = que.pop()
    time = t if time < t else time
    for d in directions:
        i, j = x+d[0], y+d[1]
        if 0<=i<N and 0<=j<M and (i,j) in unrotten:
            que.appendleft((i,j,t+1))
            unrotten.remove((i,j))

if len(unrotten) > 0:
    time = -1
print(time)