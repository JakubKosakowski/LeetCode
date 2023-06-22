class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = []
        for tab in rectangles:
            temp.append(min(tab))
        return temp.count(max(temp))
