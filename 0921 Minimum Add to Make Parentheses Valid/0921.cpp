class Solution {
public:
    int minAddToMakeValid(string s) {
        int ans = 0;
        int extra = 0;

        for (char c: s){
            if (c == '('){
                extra++;
            } else {
                if (extra == 0){
                    ans++;
                } else {
                    extra--;
                }
            }
        }

        return ans + extra;
    }
};
