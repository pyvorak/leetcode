class Solution {
public:
    int findTheLongestSubstring(string s) {
        int bitMask[26];
        bitMask['a' - 'a'] = 1 << 0;
        bitMask['e' - 'a'] = 1 << 1;
        bitMask['i' - 'a'] = 1 << 2;
        bitMask['o' - 'a'] = 1 << 3;
        bitMask['u' - 'a'] = 1 << 4;

        int EMPTY = -2;
        int seen[32];
        fill(seen, seen + 32, EMPTY);
        seen[0] = -1;

        int ans = 0;
        int cnt = 0;

        for (int i = 0; i < s.size(); i++){
            cnt ^= bitMask[s[i] - 'a'];

            if (seen[cnt] != EMPTY){
                ans =  max(ans, i - seen[cnt]);
            } else {
                seen[cnt] = i;
            }
        }

        return ans;
    }
};
