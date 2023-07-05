class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        hash = {}
        ans = 0
        for i in range(len(garbage)):
            for c in garbage[i]:
                if c not in hash:
                    hash[c] = 1
                else:
                    hash[c] += 1
        amount = len(hash.items())
        for i in range(len(garbage)):
            if i != 0:
                ans += (travel[i-1] * amount)
            for c in garbage[i]:
                ans += 1
                hash[c] -= 1
                if hash[c] == 0:
                    amount -= 1
        return ans
