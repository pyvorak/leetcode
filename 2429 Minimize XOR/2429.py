class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def b(num):
            return bin(num)[2:]
        
        def z(b, n):
            return "0" * (n - len(b)) + b

        def check(b, bit, n, inc):
            i = 0 if inc else n - 1
            while 0 <= i <= n - 1:
                if self.cnt == 0:
                    return
                if b[i] == bit:
                    self.ans[i] = '1'
                    self.cnt -= 1
                i = i + 1 if inc else i - 1
        
        b1 = b(num1)
        b2 = b(num2)
        n = max(len(b1), len(b2))
        b1 = z(b1, n)

        self.cnt = b2.count('1')
        self.ans = ['0'] * n

        check(b1, '1', n, True)
        check(b1, '0', n, False)

        return int(''.join(self.ans), 2)
