class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<bool> strong(n, true);

        for (const vector<int>& e: edges){
            int cur = e[1];
            if (strong[cur]){
                n--;
                strong[cur] = false;
                if (n == 1){
                    break;
                }
            }
        }

        return n == 1 ? find(strong.begin(), strong.end(), true) - strong.begin() : -1;
    }
};
