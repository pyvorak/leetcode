class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            p = ListNode(gcd(cur.val, cur.next.val))
            p.next = cur.next
            cur.next = p
            cur = p.next

        return head
