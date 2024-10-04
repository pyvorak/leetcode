class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        a, b = skill[0], skill[n-1]
        ans = a * b
        total = a + b

        for i in range(1, n//2):
            a, b = skill[i], skill[n-1-i]
            if a + b != total:
                return -1
            else: 
                ans += a * b

        return ans
