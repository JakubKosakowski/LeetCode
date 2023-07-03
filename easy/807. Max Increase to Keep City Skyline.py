class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        hash = {}
        ans = 0
        for row in grid:
            for i in range(len(row)):
                if i not in hash:
                    hash[i] = [row[i]]
                else:
                    hash[i].append(row[i])
        for i in range(len(grid)):
            max_row = max(grid[i])
            for j in range(len(grid[i])):
                max_col = max(hash[j])
                min_val = min(max_row, max_col)
                ans += abs(min_val - grid[i][j])
        return ans
