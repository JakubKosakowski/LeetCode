# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(start, traversal):
            if start:
                traversal = inorder(start.left, traversal)
                traversal.append(start.val)
                traversal = inorder(start.right, traversal)
            return traversal
        def inc(index, end_index, values):
            if index == 0:
                root = TreeNode(values[index])
                root.left = None
                root.right = inc(index + 1, end_index, values)
            if index > end_index:
                return None
            start = TreeNode(values[index])
            start.left = None
            start.right = inc(index + 1, end_index, values)
            return start
        values = inorder(root, [])
        return inc(0, len(values)-1, values)
