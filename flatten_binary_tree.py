class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):

            if root == None:
                return None

            lefttail = dfs(root.left)
            righttail = dfs(root.right)

            if lefttail:
                lefttail.right = root.right
                root.right = root.left
                root.left = None

            tail = righttail or lefttail or root
            return tail

        dfs(root)
