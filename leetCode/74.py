class Solution:
    from functools import reduce
    def searchMatrix(self, matrix, target) -> bool:
        def subSearch(nums, target):
            start, end = 0, len(nums)-1
            answer = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    answer = mid
                    break
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            return answer
        concatedList = reduce(lambda m, n: m+n, matrix, [])
        result = subSearch(concatedList, target)
        return True if result != -1 else False