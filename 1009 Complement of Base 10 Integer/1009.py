class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        ans = ""

        for c in b:
            if c == '1':
                ans += '0'
            else:
                ans += '1'

        return int(ans, 2)
