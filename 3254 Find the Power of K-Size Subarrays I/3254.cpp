class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        int l = -1;
        int n = nums.size();
        vector<int> ans;

        for (int i = 0; i < n; i++){
            if (i > 0 && nums[i] != nums[i-1] + 1) l = i;
            if (i >= k - 1) ans.push_back(i - l + 1 >= k ? nums[i] : -1);
        }

        return ans;
    }
};
