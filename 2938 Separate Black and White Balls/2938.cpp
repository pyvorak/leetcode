class Solution {
public:
    long long minimumSteps(string s) {
        long long ans = 0;
        long long swap = 0;

        for (char c: s){
            if (c == '1'){
                swap++;
            } else {
                ans += swap;
            }
        }

        return ans;
    }
};
