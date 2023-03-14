import sys

input = sys.stdin.readline


def backTrack(nums, idxs):
    if len(idxs) == 6:
        print(' '.join(list(map(lambda x: str(nums[x]), idxs))).strip())
    else:
        for i in range(0 if not idxs else idxs[len(idxs)-1] + 1, len(nums)):
            if len(nums)-1 - i >= 6 - (len(idxs) + 1):
                backTrack(nums, idxs + [i])

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    else:
        k = nums[0]
        backTrack(nums[1:], [])
        print()