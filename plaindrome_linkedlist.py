class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        ptr = head
        stack = []
        isPalin = True

        while(ptr != None):

            stack.append(ptr.val)
            ptr = ptr.next

        while(head != None):

            i = stack.pop()
            if(head.val == i):
                isPalin = True
            else:
                isPalin = False
                break
                
            head = head.next
        
        return isPalin
