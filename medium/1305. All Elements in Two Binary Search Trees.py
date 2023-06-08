class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(start, arr):
            if start:
                arr = inorder(start.left, arr)
                arr.append(start.val)
                arr = inorder(start.right, arr)
            return arr
        ans = inorder(root1, []) + inorder(root2, [])
        ans.sort()
        return ans
