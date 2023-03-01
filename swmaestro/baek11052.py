import sys

input = sys.stdin.readline

N = int(input())
pList = list(map(int, input().split()))

def solution(n, pList):
    for i in range(n):
        if i == 0:
            print(i, pList)
            continue
        pList[i] = max(pList[i], max([pList[i-1-j] + pList[j] for j in range((i+1)//2)]))
        print(i, pList)
    return pList[n-1]

print(solution(N,pList))