class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int ans = 1;
        int maxNum = nums[0];
        int cnt = 0;
        
        for (int num : nums) {
            if (num > maxNum) {
                maxNum = num;
                ans = cnt = 1;
            } else if (num == maxNum) {
                cnt++;
                ans = max(ans, cnt);
            } else {
                cnt = 0;
            }
        }
        
        return ans;
    }
};
