class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast, slow = head, head

        while(fast != None and fast.next != None):
            fast, slow = fast.next.next, slow.next

            if(fast == slow):
                return True
                break
                
        return False 
