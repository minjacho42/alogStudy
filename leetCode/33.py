class Solution:
    def search(self, nums, target) -> int:
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
        k = nums.index(min(nums))
        idx = subSearch(nums[k:] + nums[:k], target)
        answer = (k + idx) % len(nums) if idx != -1 else -1
        return answer