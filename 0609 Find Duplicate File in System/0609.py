class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for path in paths:
            path = path.split()
            folder = path[0]
            for s in path[1:]:
                filename, content = s.split('(')
                content = content[:-1]
                d[content].append(f"{folder}/{filename}")
        
        ans = []

        for content in d:
            if len(d[content]) > 1:
                ans.append(d[content])

        return ans
