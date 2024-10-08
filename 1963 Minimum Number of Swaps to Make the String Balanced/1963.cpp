class Solution {
public:
    int minSwaps(string s) {
        int ans = 0;
        int l = 0;
        int r = 0;

        for (char c: s){
            if (c == ']'){
                if (r == l){
                    l++;
                    ans++;
                } else {
                    r++;
                }
            } else {
                l++;
            }
        }

        return ans;
    }
};
