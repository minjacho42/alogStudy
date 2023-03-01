import sys

input = sys.stdin.readline

N = int(input())

def solution(n):
    nums = [1 for _ in range(10)]
    for _ in range(1,n):
        for i in range(10):
            nums[i] = sum(nums[i:])%10007
    return sum(nums)%10007

print(solution(N))