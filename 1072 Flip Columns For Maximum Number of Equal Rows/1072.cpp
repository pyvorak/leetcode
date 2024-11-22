class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        unordered_map<string, int> mp;
        int ans = 1;

        for (vector<int> row: matrix){
            string s = "";
            for (int c : row){
                if (row[0] == 1){
                    s += c ? '0' : '1';
                } else {
                    s += c ? '1' : '0';
                }
            }
            mp[s]++;
            ans = max(ans, mp[s]);
        }

        return ans;
    }
};
