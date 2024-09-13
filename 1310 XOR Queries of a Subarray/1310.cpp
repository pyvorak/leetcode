class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        for (int i = 1; i < arr.size(); i++){
            arr[i] ^= arr[i-1];
        }

        vector<int> ans;

        for (vector<int>& q: queries){
            int i = q[0];
            int j = q[1];
            if (i == 0){
                ans.push_back(arr[j]);
            } else {
                ans.push_back(arr[i-1] ^ arr[j]);
            }
        }

        return ans;
    }
};
