class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0

        for cnt in range(1, len(tiles)+1):
            ans += len(set(permutations(tiles, cnt)))

        return ans
