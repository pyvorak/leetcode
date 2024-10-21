class Solution {
public:
    void find(int i, int& ans, unordered_set<string>& seen, string& s){
        int n = s.size();
        if (i == n){
            ans = max(ans, (int) seen.size());
        } else if (seen.size() + n - i > ans){
            for (int j = i+1; j <= n; j++){
                string cur = s.substr(i, j-i);
                if (!seen.contains(cur)){
                    seen.insert(cur);
                    find(j, ans, seen, s);
                    seen.erase(cur);
                }
            }
        }
    }

    int maxUniqueSplit(string s) {
        unordered_set<string> seen;
        int ans = 1;
        find(0, ans, seen, s);
        return ans;
    }
};
