class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []

        def reduce():
            values = []

            while stk[-1] != '(':
                values.append(stk.pop())
            stk.pop() # remove '('
            
            op = stk.pop()

            if op == '&':
                stk.append(all(values))
            elif op == '|':
                stk.append(any(values))
            else:
                stk.append(not values[0])

        for c in expression:
            if c == ',':
                continue
            elif c != ')':
                if c == 't':
                    stk.append(True)
                elif c == 'f':
                    stk.append(False)
                else:
                    stk.append(c)
            else:
                reduce()
        
        return stk.pop()
