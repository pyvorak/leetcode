class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        ans = 1

        def gradient(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            dx = x2-x1
            dy = y2-y1
            g = gcd(dx, dy)
            return (dx//g, dy//g)

        for i in range(n):
            gradients = defaultdict(int)
            for j in range(i+1, n):
                m = gradient(points[i], points[j])
                gradients[m] += 1
                ans = max(ans, gradients[m]+1)

        return ans
