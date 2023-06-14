# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def preorder(start, trav):
            if start:
                trav.append(start.val)
                trav = preorder(start.left, trav)
                trav = preorder(start.right, trav)
            return trav
        temp = preorder(root, [])
        temp.sort()
        ans = max(temp)
        for i in range(len(temp)-1):
            ans = min(ans, abs(temp[i]-temp[i+1]))
        return ans
