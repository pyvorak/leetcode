class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k
        cur = head
        n = 0
        
        while cur:
            cur = cur.next
            n += 1
        
        avg = n // k
        extra = n % k
        cur = head

        for i in range(k):
            ans[i] = cur
            cnt = avg 

            if extra:
                cnt += 1
                extra -= 1

            while cur and cnt > 1:
                cur = cur.next
                cnt -= 1

            if cur:
                prev = cur
                cur = cur.next
                prev.next = None

        return ans
