class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 3
        
        small = [-x for x in nums[:k]]
        heapify(small)
        a = sum(nums[:k])
        l = [a]

        for x in nums[k:k*2]:
            a += x
            heappush(small, -x)
            cur = heappop(small)
            a += cur
            l.append(a)

        big = nums[-k:]
        heapify(big)
        b = sum(nums[-k:])
        r = [b]
        
        for x in nums[k:k*2][::-1]:
            b += x
            heappush(big, x)
            cur = heappop(big)
            b -= cur
            r.append(b)
            
        return min([x - y for x, y in zip(l, r[::-1])])
        
            
