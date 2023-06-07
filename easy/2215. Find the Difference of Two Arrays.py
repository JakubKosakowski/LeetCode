class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = [list(), list()]
        for n in set1:
            if n not in set2:
                ans[0].append(n)
        for n in set2:
            if n not in set1:
                ans[1].append(n)
        return ans
