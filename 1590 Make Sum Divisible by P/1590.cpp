class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        int target = 0;

        for (int i = 0; i<n; i++){
            target = (target + nums[i]) % p;
        }

        if (target == 0){
            return 0;
        }

        int ans = n;
        unordered_map<int,int> mp;
        mp[0] = -1;
        int cur = 0;

        for (int i = 0; i<n; i++){
            cur = (cur + nums[i]) % p;
        
            int prev = (cur - target + p) % p;
            if (mp.find(prev) != mp.end()){
                ans = min(ans, i - mp[prev]);
            }

            mp[cur] = i;
        }

        return ans == n ? -1 : ans;
    }
};
