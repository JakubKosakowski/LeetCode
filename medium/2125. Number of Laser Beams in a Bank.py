class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        check_row = 0
        for i in range(len(bank)):
            if bank[i].count("1") != 0:
                if check_row == 0:
                    check_row = bank[i].count("1")
                    continue
                else:
                    ans += (check_row * bank[i].count("1"))
                    check_row = bank[i].count("1")
        return ans
