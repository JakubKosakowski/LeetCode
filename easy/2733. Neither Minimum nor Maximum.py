class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi, mx = min(nums), max(nums)
        for num in nums:
            if num != mi and num != mx:
                return num
        return -1
