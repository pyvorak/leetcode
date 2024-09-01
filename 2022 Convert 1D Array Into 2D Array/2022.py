class Solution:
    def construct2DArray(self, a: List[int], m: int, n: int) -> List[List[int]]:
        return [a[i * n:(i + 1) * n] for i in range(m)] if len(a) == m * n else []
