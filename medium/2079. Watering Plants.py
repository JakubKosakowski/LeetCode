class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        temp = capacity
        for i in range(len(plants)):
            if temp >= plants[i]:
                ans += 1
                temp -= plants[i]
            else:
                ans += (2 * i) + 1
                temp = capacity - plants[i]
        return ans
