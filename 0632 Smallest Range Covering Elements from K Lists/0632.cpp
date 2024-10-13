class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> minHeap;
        int maxVal = -pow(10, 6);

        for (int i = 0; i < nums.size(); i++){
            int val = nums[i][0];
            minHeap.push({val, i, 0});
            maxVal = max(maxVal, val);
        }

        vector<int> ans = {(int) -pow(10, 6), (int) pow(10, 6)};

        while (!minHeap.empty()){
            int val = minHeap.top()[0];
            int i = minHeap.top()[1];
            int j = minHeap.top()[2];
            minHeap.pop();

            if (maxVal - val < ans[1] - ans[0]){
                ans = {val, maxVal};
            }

            if (j + 1 < nums[i].size()){
                int nextVal = nums[i][j+1];
                minHeap.push({nextVal, i, j+1});
                maxVal = max(maxVal, nextVal);
            } else {
                break;
            }
        }

        return ans;
    }
};
