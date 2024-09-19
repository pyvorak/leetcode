class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp = {}

        def find(s):
            if s in dp:
                return dp[s]
            
            ans = []

            for i in range(len(s)):
                if s[i] in "+-*":
                    op = s[i]
                    left = find(s[:i]) 
                    right = find(s[i+1:])
                    for l in left:
                        for r in right:
                            if op == '+':
                                ans.append(l + r)
                            elif op == '-':
                                ans.append(l - r)
                            elif op == '*':
                                ans.append(l * r)
            
            if len(ans) == 0:
                ans.append(int(s))

            dp[s] = ans
            return ans
                    

        return find(expression)
