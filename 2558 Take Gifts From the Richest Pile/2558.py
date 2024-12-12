class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        
        for i in range(k):
            num = heapq.heappop(gifts)
            num = -num
            num = math.floor(math.sqrt(num))
            heapq.heappush(gifts, -num)
            
        return -sum(gifts)

