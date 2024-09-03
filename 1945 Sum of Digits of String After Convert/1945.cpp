class Solution {
public:
    int getLucky(string s, int k) {
        int ans = 0;

        for (char c: s){
            int num = c - 'a' + 1;
            if (num >= 10) num = num / 10 + num % 10;
            ans += num;
        }

        while (--k){
            int cur = ans;
            ans = 0; 
            while (cur){
                ans += cur % 10;
                cur /= 10;
            }
        }
        
        return ans;
    }
};
