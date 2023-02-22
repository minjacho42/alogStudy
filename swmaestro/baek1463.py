from collections import deque 
def solution(num):
    que = deque()
    que.appendleft((num, 0))
    while len(que) > 0:
        num, count = que.pop()
        if num == 1:
            return count
        if not num % 3:
            que.appendleft((num//3, count+1))
        if not num % 2:
            que.appendleft((num//2, count+1))
        que.appendleft((num-1, count+1))

if __name__ == '__main__':
    print(solution(int(input())))
