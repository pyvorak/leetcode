class Solution {
public:
    int get_max_beauty(vector<vector<int>>& items, int max_price){
        int ans = 0;

        int l = 0; 
        int r = items.size() - 1;

        while (l <= r){
            int m = (l + r) / 2;
            int price = items[m][0];
            int beauty = items[m][1];

            if (price > max_price){
                r = m - 1;
            } else {
                ans = max(ans, beauty);
                l = m + 1;
            }
        }

        return ans;
    }

    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        sort(items.begin(), items.end());

        int max_beauty = 0;

        for (int i = 0; i < items.size(); i++){
            max_beauty = max(max_beauty, items[i][1]);
            items[i][1] = max_beauty;
        }

        int n = queries.size();
        vector<int> ans(n);

        for (int i = 0; i < n; i++){
            ans[i] = get_max_beauty(items, queries[i]);
        }
    
        return ans;
    }
};

