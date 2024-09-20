class Solution {
public:
    string shortestPalindrome(string s) {
        int i = 0;
        int n = s.size();

        for (int j = n-1; j >= 0; j--){
            if (s[i] == s[j]){
                i++;
            }
        }

        if (i == n){
            return s;
        }

        string mid = s.substr(0, i);
        string r = s.substr(i);
        string l = r;
        reverse(l.begin(), l.end());

        return l + shortestPalindrome(mid) + r;
    }
};
