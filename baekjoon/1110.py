import sys

input = sys.stdin.readline

N = int(input())

def solution(n):
    answer = 1
    n1, n2 = n, (n % 10) * 10 + (sum(map(int,list(str(n)))))%10
    while n2 != n:
        n1, n2 = n2, (n2 % 10) * 10 + (sum(map(int,list(str(n2)))))%10
        answer += 1
    return answer

print(solution(N))