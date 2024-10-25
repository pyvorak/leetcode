class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []
        prev = " "

        for f in folder:
            if not f.startswith(prev + '/'):
                ans.append(f)
                prev = f

        return ans
