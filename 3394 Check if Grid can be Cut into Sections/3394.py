class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = sorted([[x1, x2] for x1, y1, x2, y2 in rectangles])
        y = sorted([[y1, y2] for x1, y1, x2, y2 in rectangles])

        def valid(a):
            cnt = prev =  0
            
            for start, end in a:
                if start >= prev:
                    cnt += 1
                    if cnt >= 3:
                        return True

                prev = max(prev, end)
    
            return False

        return valid(x) or valid(y)
