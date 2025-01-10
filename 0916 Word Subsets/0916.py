class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt = Counter()

        for word in words2:
            for c, freq in Counter(word).items():
                cnt[c] = max(cnt[c], freq)
        
        ans = []

        def valid(word, cnt):
            cur = Counter(word)

            for c, freq in cnt.items():
                if freq > cur[c]:
                    return False
            
            return True
            
        return [word for word in words1 if valid(word, cnt)]
