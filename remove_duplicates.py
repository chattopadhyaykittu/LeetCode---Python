class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev_ptr,ptr = None, head
        duplicate_dict = dict()

        while ptr:

            if(ptr.val not in duplicate_dict):
                duplicate_dict[ptr.val] = 0
                prev_ptr = ptr
            else:
                prev_ptr.next = ptr.next
            
            ptr = ptr.next

        return head
