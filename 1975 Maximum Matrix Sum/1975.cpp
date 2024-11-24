class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long ans = 0;
        int smallest = INT_MAX;
        int negativeCount = 0;

        for (int i = 0; i < matrix.size(); i++){
            for (int j = 0; j < matrix[0].size(); j++){
                int cur = matrix[i][j];
                if (matrix[i][j] < 0){
                    negativeCount++;
                }
                cur = abs(cur);
                ans += cur;
                smallest = min(smallest, cur);
            }
        }

        if (negativeCount % 2 == 0){
            return ans;
        } else {
            return ans - 2 * smallest;
        }
    }
};
