import sys

input = sys.stdin.readline

x, y = tuple(map(int, input().split()))

def solution(x, y):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return days[(sum(months[:x-1]) + y)%7]

print(solution(x,y))