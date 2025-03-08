class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = cur = blocks[:k].count('W')

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                cur += 1
            if blocks[i-k] == 'W':
                cur -= 1
            ans = min(ans, cur)

        return ans
