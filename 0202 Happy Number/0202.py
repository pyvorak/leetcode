class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            return sum([int(c)**2 for c in str(num)])

        fast, slow = next_num(n), n

        while fast != 1 and fast != slow:
            fast = next_num(next_num(fast))
            slow = next_num(slow)
        
        return fast == 1
