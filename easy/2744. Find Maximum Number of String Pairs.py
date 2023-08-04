class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        hash = {}
        ans = 0
        for word in words:
            if word[::-1] not in hash:
                hash[word] = 1
            else:
                ans += 1
        return ans
