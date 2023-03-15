import  sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())
K = int(input())
apples = set()
for _ in range(K):
    i, j = map(int, input().split())
    apples.add((i,j))
L = int(input())
cmds = defaultdict(str)
for _ in range(L):
    sec, d = input().split()
    sec = int(sec)
    cmds[sec] = d

def solution(n, apples, cmds):
    print(n, apples, cmds)
    snake = deque([(1,1)])
    directions = [(0, 1),(-1,0),(0, -1),(1 ,0)]
    cur = (1,1)
    curD = 0
    time = 0
    while True:
        if time in cmds:
            if cmds[time] == 'L':
                curD = (curD + 1)%4
            else:
                curD = (curD - 1)%4
        cur = tuple(map(sum, zip(cur, directions[curD])))
        if cur in set(snake) or not (0<cur[0]<=n and 0<cur[1]<=n):
            break
        snake.append(cur)
        if cur in apples:
            apples -= set([cur])
        else:
            snake.popleft()
        time+=1
        print(snake, curD, time)
    return time

print(solution(N,apples,cmds) + 1)