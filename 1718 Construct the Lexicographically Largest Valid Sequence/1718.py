class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [None] * (n*2-1)
        done = [False] * n

        def dfs(idx):
            if idx == len(ans):
                return True

            if ans[idx] is not None:
                return dfs(idx+1)

            for i in range(n-1, -1, -1):
                if not done[i]:
                    num = i + 1 
                    if num == 1:
                        done[i] = True
                        ans[idx] = num
                        if dfs(idx+1):
                            return True
                        done[i] = False
                        ans[idx] = None
                    else:
                        if idx + num < len(ans) and ans[idx+num] is None:
                            done[i] = True
                            ans[idx] = num
                            ans[idx+num] = num
                            if dfs(idx+1):
                                return True
                            done[i] = False
                            ans[idx] = None
                            ans[idx+num] = None
            return False

        dfs(0)
        return ans
