class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            # linked list has 0 or 1 nodes
            return None

        if not head.next.next:
            # linked list has 2 nodes
            head.next = None
            return head


        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next


        prev.next = slow.next

        return head 
