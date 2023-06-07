class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_trees(t1, t2):
            if not t1:
                return t2
            if not t2:
                return t1
            t1.val += t2.val
            t1.left = merge_trees(t1.left, t2.left)
            t1.right = merge_trees(t1.right, t2.right)
            return t1
        return merge_trees(root1, root2)
