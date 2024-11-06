class Solution {
public:
    int bit_count(int x) {
        int count = 0;
        while (x) {
            count += x & 1;
            x /= 2;
        }
        return count;
    }

    bool canSortArray(vector<int>& nums) {
        vector<pair<int,int>> ans;

        int small = nums[0];
        int big = nums[0];
        int prev = bit_count(nums[0]);

        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            int cur = bit_count(num);
            
            if (cur == prev){
                small = min(small, num);
                big = max(big, num);
            } else {
                ans.push_back({small, big});
                small = num;
                big = num;
            }
            prev = cur;
        }
        ans.push_back({small, big});

        for (int i = 1; i < ans.size(); i++){
            if (ans[i-1].second > ans[i].first){
                return false;
            }
        }
        
        return true;
    }
};
