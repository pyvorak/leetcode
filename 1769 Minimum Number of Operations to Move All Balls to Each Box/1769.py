class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = l_cnt = 0
        r = boxes.count('1')
        r_cnt = sum(i for i, c in enumerate(boxes) if c == '1')

        ans = []

        for c in boxes:
            ans.append(l_cnt + r_cnt)
            
            if c == "1":
                l += 1
                r -= 1
            
            l_cnt += l
            r_cnt -= r
            
        
        return ans
