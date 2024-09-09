# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        cur = head
        c1, c2 = 0, n-1
        r1, r2 = 0, m-1

        while cur and c1 <= c2 and r1 <= r2:
            j = c1
            while cur and j <= c2:
                ans[r1][j] = cur.val
                j += 1
                cur = cur.next
            
            i = r1 + 1
            while cur and i <= r2:
                ans[i][c2] = cur.val
                i += 1
                cur = cur.next

            j = c2 - 1
            while cur and j >= c1:
                ans[r2][j] = cur.val
                j -= 1
                cur = cur.next
            
            i = r2 - 1
            while cur and i >= r1 + 1:
                ans[i][c1] = cur.val
                i -= 1
                cur = cur.next

            c1 += 1
            c2 -= 1
            r1 += 1
            r2 -= 1
        
        return ans

        
