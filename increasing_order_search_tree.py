class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        dummy = curr = TreeNode()
        stack = []

        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            curr.right = root

            curr = curr.right
            root = root.right

            curr.left = None

        return dummy.right
