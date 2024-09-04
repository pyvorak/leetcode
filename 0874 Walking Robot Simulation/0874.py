class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, z, ans = 0, 0, 0, 0
        invalid = set()

        for i, j in obstacles:
            invalid.add((i, j))

        for command in commands:
            if command < 0:
                z = (z + 1 if command == -1 else z + 3) % 4
            else:
                dx, dy = ((0, 1), (1, 0), (0, -1), (-1, 0))[z]
                while command > 0:
                    x, y = x + dx, y + dy
                    if (x, y) in invalid:
                        x, y = x - dx, y - dy
                        break
                    command -= 1
            ans = max(ans, x ** 2 + y ** 2)

        return ans
