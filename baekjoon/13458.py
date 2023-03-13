import sys
from math import ceil

input = sys.stdin.readline

n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())

print(sum(map(lambda x: ceil((x-b if x > b else 0)/c), rooms)) + len(rooms))