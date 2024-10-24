class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []

        for w in path.split('/'):
            if w == '..':
                if stk:
                    stk.pop()
            elif w not in ['', '.']:
                stk.append(w)

        return f"/{'/'.join(stk)}"
