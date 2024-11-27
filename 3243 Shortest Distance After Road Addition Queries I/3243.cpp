class Solution {
public:
    void dfs(vector<vector<int>>& prevRoads, vector<int>& dp, int cur){
        int shortcut = dp[cur] + 1;

        for (int prev: prevRoads[cur]){
            if (dp[prev] < shortcut) continue;
            dp[prev] = shortcut;
            dfs(prevRoads, dp, prev);
        }
    }

    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> prevRoads(n);
        vector<int> dp(n);

        int m = queries.size();
        vector<int> ans(m);

        for (int i = 0; i < n; i++){
            dp[i] = n - 1 - i;
        }

        for (int i = 0; i < n - 1; i++){
            prevRoads[i+1].push_back(i);
        }

        for (int i = 0; i < m; i++){
            int u = queries[i][0];
            int v = queries[i][1];
            prevRoads[v].push_back(u);

            int shortcut = dp[v] + 1;
            if (shortcut < dp[u]){
                dp[u] = shortcut;
                dfs(prevRoads, dp, u);
            }

            ans[i] = dp[0];
        }

        return ans;
    }
};
