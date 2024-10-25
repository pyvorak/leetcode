class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());       
        vector<string> ans;

        for (string f: folder){
            if (ans.empty() || !f.starts_with(ans.back() + "/")) {
                ans.push_back(f);
            }
        }

        return ans;
    }
};
