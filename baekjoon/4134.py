from math import sqrt
n = int(input())
nums = [int(input()) for __ in range(n)]
for num in nums:
    if num <= 2:
        print(2)
        continue
    while True:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                num += 1
                break
        else:
            print(num)
            break
