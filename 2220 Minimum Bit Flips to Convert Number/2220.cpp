class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans = 0;
        int flips = start ^ goal;
        
        while (flips){
            ans += flips & 1;
            flips /= 2;
        }

        return ans;
    }
};
