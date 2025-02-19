class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        ans = []

        def dfs(s):
            if len(ans) >= k:
                return
            
            if len(s) == n:
                ans.append(s)
                return
            
            for c in chars:
                if s[-1] != c:
                    dfs(s+c)

        
        for c in chars:
            dfs(c)

        return "" if len(ans) < k else ans[-1]
