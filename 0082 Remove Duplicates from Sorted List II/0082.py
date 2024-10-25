class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0, head)
        prev, cur = start, head

        while cur:
            if not cur.next or cur.next.val != cur.val:
                prev = cur
            else:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
            cur = cur.next

        return start.next
