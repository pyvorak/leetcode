class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        vector<int> bins(24, 0);

        for (int x: candidates){
            int i = 0;
            while (x){
                bins[i++] += x & 1;
                x /= 2;
            }
        }
        
        return *max_element(bins.begin(), bins.end());
    }
};
