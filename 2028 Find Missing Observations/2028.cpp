class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int sum = (n + rolls.size()) * mean - accumulate(rolls.begin(), rolls.end(), 0);
        if (sum < n || sum> 6 * n) return {};
        int q = sum / n, r = sum % n; 
        vector<int> ans(n, q);
        for (int i = 0; i < r; i++) ans[i]++;
        return ans;
    }
};
