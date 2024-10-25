class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        copy_map = {None: None}
        
        cur = head
        while cur:
            copy_map[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy_map[cur].next = copy_map[cur.next]
            copy_map[cur].random = copy_map[cur.random]
            cur = cur.next

        return copy_map[head]
