class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ans = p = c = ListNode(0, head); bad = set(nums)
        while c := c.next : p.next, p = (c.next, p) if c.val in bad else (p.next, p.next)
        return ans.next
