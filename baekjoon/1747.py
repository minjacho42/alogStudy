import sys, math

input = sys.stdin.readline

n = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True
    
def solution(n):
    answer = n
    while not (int(str(answer)[::-1]) == answer and is_prime(answer)):
        answer += 1
    return answer

print(solution(n))