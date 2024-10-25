class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head, more_head = ListNode(0), ListNode(0)
        less, more = less_head, more_head
        cur = head

        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                more.next = cur
                more = more.next
            cur = cur.next
        
        less.next = more_head.next
        more.next = None

        return less_head.next
