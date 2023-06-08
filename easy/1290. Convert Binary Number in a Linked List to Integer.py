# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def count(start, arr):
            if start:
                arr.append(start.val)
                count(start.next, arr)
            return arr
        ans = 0
        tab = count(head, [])
        for i in range(len(tab)):
            ans += (tab[i] * (2 ** (len(tab) - 1 - i)))
        return ans
