class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        int ans = -1;
        sort(nums.begin(), nums.end());

        vector<bool> seen(100001, false);

        for (int num: nums){
            seen[num] = true;
        }

        int n = nums.size();

        for (int i = 0; i < n; i++){
            int cnt = 1;
            long long nextNum = (long long) nums[i] * nums[i];

            while (nextNum <= nums[n-1] && seen[nextNum]){
                cnt++;
                nextNum *= nextNum;
            }
            
            if (cnt >= 2){    
                ans = max(ans, cnt);
            }
        }

        return ans;
    }
};
