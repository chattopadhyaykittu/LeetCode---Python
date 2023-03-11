class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre_ptr, cur = None, head

        while cur:
            temp = cur.next
            cur.next = pre_ptr
            pre_ptr = cur
            cur = temp
        
        return pre_ptr
