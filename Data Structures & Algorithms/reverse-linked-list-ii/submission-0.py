class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        #move the curr pointer to the left node
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next

        #reverse nodes between left and right
        prev = None
        for i in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        #update the pointers
        leftPrev.next.next = curr #curr is node after "right"
        leftPrev.next = prev #prev is "right"
        return dummy.next