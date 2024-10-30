class Solution {
public:
    vector<int> find(vector<int>& nums){
        vector<int> v(nums.size(), 1);
        
        for (int i = 0; i < nums.size(); i++){
            for (int j = 0; j < i; j++){
                if (nums[i] > nums[j]){
                    v[i] = max(v[i], v[j] + 1);
                }
            }
        }

        return v;
    }

    int minimumMountainRemovals(vector<int>& nums) {
        int n = nums.size();

        vector<int> left = find(nums);
        
        reverse(nums.begin(), nums.end());
        vector<int> right = find(nums);
        reverse(right.begin(), right.end());
        
        int ans = 0;

        for (int i = 1; i <= n-2; i++){
            if (left[i] > 1 && right[i] > 1){
                ans = max(ans, left[i] + right[i] - 1);
            }
        }

        return n - ans;
    }
};
