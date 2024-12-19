class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        i, chunks, max_element = 0, 0, 0
        n = len(arr)
    
        for i in range(n):
            max_element = max(max_element, arr[i])
            if i == max_element:
                chunks += 1

        return chunks

