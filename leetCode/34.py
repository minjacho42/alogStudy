class Solution:
    def searchRange(self, nums, target):
        answer = [-1,-1]
        def searchMid(nums, target):
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
        mid = searchMid(nums, target)
        if mid == -1:
            return answer 
        answer = [mid,mid]
        while True:
            result = searchMid(nums[:answer[0]],target)
            if result != -1:
                answer[0] = result
            else:
                break
        while True:
            result = searchMid(nums[answer[1]+1:],target)
            if result != -1:
                answer[1] = answer[1] + 1 + result
            else:
                break
        return answer