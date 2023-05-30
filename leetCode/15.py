#%%
"""Solution got timeout"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def binarySearch(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                return False
        sortedNums = sorted(nums)
        start, end = 0, len(sortedNums) - 1
        answer = []
        #print(sortedNums)
        for start in range(0,len(sortedNums) - 2):
            for end in range(len(sortedNums) - 1, start + 1, -1):
                #print(sortedNums[start + 1: end], -(sortedNums[end] + sortedNums[start]))
                if binarySearch(sortedNums[start + 1: end], -(sortedNums[end] + sortedNums[start])):
                    newElement = [sortedNums[start], sortedNums[end], -(sortedNums[end] + sortedNums[start])]
                    if newElement not in answer:
                        answer.append(newElement)
        return answer
#%%
""" Use 'set' to recover timeout """

class Solution:
    from itertools import combinations
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        posNums, negNums, zeroNums  = list(filter(lambda x : x > 0, nums)), list(filter(lambda x : x < 0, nums)) , list(filter(lambda x : x == 0, nums))
        #print(posNums, negNums, zeroNums)
        setPosNums, setNegNums = set(posNums), set(negNums)
        for posComb in set(combinations(sorted(posNums), 2)):
            if -sum(posComb) in setNegNums:
                answers.append(list(posComb) + [-sum(posComb)])
        for negComb in set(combinations(sorted(negNums), 2)):
            if -sum(negComb) in setPosNums:
                answers.append(list(negComb) + [-sum(negComb)])
        if zeroNums:
            for num in set(posNums) & set(map(abs,negNums)):
                answers.append([num,0,-num])
            if len(zeroNums) > 2 :
                answers.append([0,0,0])
        return answers