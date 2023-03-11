import sys

input = sys.stdin.readline

_ = input()
sign = list(input().split())

def big(sign, answer):
    if len(answer) < 1:
        for n in range(9, -1, -1):
            result = big(sign, [n])
            if result:
                return result
    else:
        if sign[0] == '>':
            for n in range(answer[len(answer)-1]-1, -1, -1):
                if n not in answer:
                    if len(sign) > 1:
                        result = big(sign[1:], answer+[n])
                        if result:
                            return result
                    else:
                        return answer+[n]
        else:
            for n in range(9, answer[len(answer)-1], -1):
                if n not in answer:
                    if len(sign) > 1:
                        result = big(sign[1:], answer+[n])
                        if result:
                            return result
                    else:
                        return answer+[n]
                    
def small(sign, answer):
    if len(answer) < 1:
        for n in range(0, 10):
            result = small(sign, [n])
            if result:
                return result
    else:
        if sign[0] == '>':
            for n in range(0, answer[len(answer)-1]):
                if n not in answer:
                    if len(sign) > 1:
                        result = small(sign[1:], answer+[n])
                        if result:
                            return result
                    else:
                        return answer+[n]
        else:
            for n in range(answer[len(answer)-1]+1, 10):
                if n not in answer:
                    if len(sign) > 1:
                        result = small(sign[1:], answer+[n])
                        if result:
                            return result
                    else:
                        return answer+[n]

for result in [big(sign,[]), small(sign,[])]:
    print(''.join(map(str,result)))