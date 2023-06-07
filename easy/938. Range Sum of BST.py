class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(start, ans):
            if start:
                ans = inorder(start.left, ans)
                if low <= start.val <= high:
                    ans += start.val
                ans = inorder(start.right, ans)
            return ans
        return inorder(root, 0)
