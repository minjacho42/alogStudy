class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if nums[end] > nums[start]:
            return nums[0]
        while start < end:
            mid = (start+end)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
        return nums[start]