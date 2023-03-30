class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        cheat = []

        curr = list1

        while curr:
            cheat.append(curr.val)
            curr = curr.next

        cheat2 = []

        curr = list2

        while curr:
            cheat2.append(curr.val)
            curr = curr.next

        cheat3 = cheat[: a] + cheat2 + cheat[b+1:]

        if len(cheat3) == 0:
            return None

        head = ListNode(cheat3[0])
        curr = head

        for x in cheat3[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        
        return head 
