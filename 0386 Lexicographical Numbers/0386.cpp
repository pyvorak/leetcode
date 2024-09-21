class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int num = 1;
        int left = n;

        while (left--){
            ans.push_back(num);
            if (num * 10 <= n){
                num *= 10;
            } else {
                while (num % 10 == 9 || num + 1 > n){
                    num /= 10;
                }
                num++;
            }
        }

        return ans;
    }
};
