class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        while True:
            temp = []
            new = []
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                else:
                    new.append(nums[i])
            ans.append(temp)
            nums = new
            if nums == []:
                break
        return ans
