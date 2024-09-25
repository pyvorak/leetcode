class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = defaultdict(int)

        for word in words:
            for i in range(1, len(word)+1):
                d[word[:i]] += 1
        
        ans = []

        for word in words:
            cnt = 0
            for i in range(1, len(word)+1):
                cnt += d[word[:i]]
            ans.append(cnt)

        return ans
