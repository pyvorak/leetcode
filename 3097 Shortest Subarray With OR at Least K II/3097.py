class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        BIT_LEN = 32
        bits = [0] * BIT_LEN

        def add(num):
            for i in range(BIT_LEN):
                if num & 1 << i:
                    bits[i] += 1
        
        def remove(num, cur):
            for i in range(BIT_LEN):
                b = 1 << i
                if num & b:
                    bits[i] -= 1
    
                    if bits[i] == 0:
                        cur -= b

            return cur
                

        n = len(nums)
        l = 0
        cur = 0
        
        INF = float('inf')
        ans = INF

        for r in range(n):
            num = nums[r]
            cur |= num
            add(num)

            while cur >= k and l <= r:
                ans = min(ans, r - l + 1)
                cur = remove(nums[l], cur)
                l += 1

        return -1 if ans == INF else ans
