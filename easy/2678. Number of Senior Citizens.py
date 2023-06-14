class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for ele in details:
            ans += 1 if int(ele[-4:-2]) > 60 else 0
        return ans
