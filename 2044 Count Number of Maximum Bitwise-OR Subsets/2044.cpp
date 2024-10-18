class Solution {
public:
    void find(vector<int>& nums, int i, int val, int& maxOr, int& ans){
        if (i == nums.size()) {
            if (val == maxOr) ans++;
        } else {
            find(nums, i+1, val, maxOr, ans);
            find(nums, i+1, val | nums[i], maxOr, ans); 
        }
    }

    int countMaxOrSubsets(vector<int>& nums) {
        int maxOr = 0;

        for (int num: nums) maxOr |= num;

        int ans = 0;

        find(nums, 0, 0, maxOr, ans);

        return ans;
    }
};
