class Solution {
public:
    bool validRow(vector<vector<int>>& grid, int row){
        return row >= 0 && row < grid.size();
    }
    
    void find(vector<vector<int>>& grid, vector<vector<int>>& dp, int r, int c, int& ans){
        int m = grid.size();
        int n = grid[0].size();
        
        if (c < n - 1) {
            int nextCnt = dp[r][c] + 1;
            int nextC = c + 1;
            for (int nextR = r-1; nextR <= r+1; nextR++){
                if (validRow(grid, nextR) && nextCnt > dp[nextR][nextC] && grid[r][c] < grid[nextR][nextC]){  
                    ans = max(ans, nextCnt);
                    dp[nextR][nextC] = nextCnt;
                    find(grid, dp, nextR, nextC, ans);
                }
            }   
        }
    }

    int maxMoves(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));

        int ans = 0;

        for (int r = 0; r < m; r++){
            find(grid, dp, r, 0, ans);
        }

        return ans;
    }
};
