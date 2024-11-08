class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int maxValue = pow(2, maximumBit) - 1;
        int cur = 0;

        for (int num: nums){
            cur ^= num;
        }

        vector<int> ans;
        int n = nums.size();
        
        for (int i = n-1; i>=0; i--){
            int k = maxValue ^ cur;
            ans.push_back(k);
            cur ^= nums[i];
        }
        
        return ans;
    }
};
