class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash:
                if t[i] in [*hash.values()]:
                    return False
                else:
                    hash[s[i]] = t[i]
                    continue
            if t[i] != hash[s[i]]:
                return False
        return True
