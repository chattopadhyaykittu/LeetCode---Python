class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None
    
    # Find the middle node of the linked list
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
    
    # Create a new tree node with the value of the middle node
        root = TreeNode(slow.val)
    
    # Recursively build the left subtree
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
    
    # Recursively build the right subtree
        root.right = self.sortedListToBST(slow.next)
    
        return root
