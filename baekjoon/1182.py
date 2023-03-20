N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

def dfs(nums, s):
    global answer
    for i, num in enumerate(nums):
        if s == num:
            answer += 1
        dfs(nums[i+1:], s - num)

dfs(nums, S)
print(answer)