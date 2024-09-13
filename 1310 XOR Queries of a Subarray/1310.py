class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        ans = []

        for i, j in queries:
            if i == 0:
                ans.append(arr[j])
            else:
                ans.append(arr[i-1] ^ arr[j])

        return ans
