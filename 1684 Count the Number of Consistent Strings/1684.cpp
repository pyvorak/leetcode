class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        vector<bool> valid(26, false);
        
        for (char c: allowed){
            valid[c - 'a'] = true;
        }

        int ans = 0;

        for (string word: words){
            bool is_consistent = true;
            
            for (char c: word){
                if (!valid[c - 'a']){
                    is_consistent = false;
                    break;
                }
            }

            if (is_consistent){
                ans++;
            }
        }

        return ans;
    }
};
