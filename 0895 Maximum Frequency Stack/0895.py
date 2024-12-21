class FreqStack:

    def __init__(self):
        self.stk = [[]]
        self.count = Counter()
        

    def push(self, val: int) -> None:
        f = self.count[val]
        self.count[val] += 1

        if f == len(self.stk):
            self.stk.append([])

        self.stk[f].append(val)
        
    def pop(self) -> int:
        val = self.stk[-1].pop()

        if not self.stk[-1]:
            self.stk.pop()
            
        self.count[val] -= 1
        return val
