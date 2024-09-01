# define VD vector<double>

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& probs, int start, int end) {
        VD dp(n, 0.0); dp[start] = 1.0;

        while (n--){
            bool valid = false;
            for (int i = 0; i < edges.size(); i++){
                int u = edges[i][0], v = edges[i][1];
                double p = probs[i];
                if (dp[u]*p > dp[v]){
                    dp[v] = dp[u]*p;
                    valid = true;
                }
                if (dp[v]*p > dp[u]){
                    dp[u] = dp[v]*p;
                    valid = true;
                }
            }
            if (!valid) break;
        }

        return dp[end];
    }
};
