class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(head == None and head.next == None):
            return head

        ans = ListNode(-1)
        res = ans

        temp = head

        while temp:
            if temp.val != 0:
                sum = 0
                while(temp.next != None and temp.val != 0):
                    sum += temp.val
                    temp = temp.next

                new_node = ListNode(sum)
                res.next = new_node
                res = res.next

            temp = temp.next

        return ans.next

