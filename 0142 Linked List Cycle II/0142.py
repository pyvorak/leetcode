class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        f, s = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                break
        else:
            return None
        
        s = head
        while s != f:
            s = s.next
            f = f.next
        return s
