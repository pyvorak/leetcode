class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        i, chunks, max_element = 0, 0, 0
        
        for i in range(len(arr)):
            max_element = max(max_element, arr[i])
            if i == max_element:
                chunks += 1

        return chunks
