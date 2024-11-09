class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def int_to_binary(x):
            return bin(x)[2:]
        
        def binary_list_to_int(a):
            return int("".join(ans), 2)
        
        binary = int_to_binary(x)
        zero = binary.count('0')
        choices = 2**zero

        
        front = (n-1) // choices if choices > 0 else n-1
        front_binary = int_to_binary(front) if front > 0 else ""
        
        ans = list(front_binary + binary)
        
        back_binary = int_to_binary((n-1) % choices) if choices > 1 else ""

        i = len(ans) - 1

        for c in back_binary[::-1]:
            while ans[i] == '1':
                i -= 1

            if c == '1':
                ans[i] = '1'
            
            i -= 1
        
        return binary_list_to_int(ans)
