def solution(N, number):
    setList = [set(),]
    for used in range(1,9):
        curSet = set()
        curSet.add(int(str(N) * used)) # N이 두자리수 이상일 경우 고려 필수.
        for i in range(1, used):
            for el1 in setList[i]:
                for el2 in setList[used-i]:
                    curSet.add(el1 + el2)
                    curSet.add(el1 - el2)
                    curSet.add(el1 * el2)
                    if el2 != 0:
                        curSet.add(el1 // el2)
        if number in curSet:
            return used
        setList.append(curSet)
    return -1