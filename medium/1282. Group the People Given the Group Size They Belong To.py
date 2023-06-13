class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash = {}
        ans = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in hash:
                hash[groupSizes[i]] = [i]
            else:
                hash[groupSizes[i]].append(i)
        for key in hash:
            temp = int(key)
            for i in range(0, len(hash[key]), temp):
                ans.append(hash[key][i:i+temp])
        return ans
