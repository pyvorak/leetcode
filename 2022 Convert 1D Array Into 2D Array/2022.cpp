class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& a, int m, int n) {
        if (m*n != a.size()) return {};
        vector<vector<int>> ans(m, vector<int>(n));
        int k = 0; 
        for (int i = 0; i<m; i++){
            for (int j = 0; j<n; j++){
                ans[i][j] = a[k++];
            }   
        }
        return ans;
    }
};
