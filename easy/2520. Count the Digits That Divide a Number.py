class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        temp = list(str(num))
        for c in temp:
            ans += 1 if num % int(c) == 0 else 0
        return ans
