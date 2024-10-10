class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        stack<int> stk;
        
        for (int i = 0; i < nums.size(); i++){
            if (stk.empty() || nums[stk.top()] > nums[i]){
                stk.push(i);
            } 
        }

        int ans = 0;

        for (int i = nums.size() - 1; i >= 0; i--){
            while (!stk.empty() && nums[stk.top()] <= nums[i]){
                ans = max(ans, i - stk.top());
                stk.pop();
            }
        }

        return ans;
    }
};
