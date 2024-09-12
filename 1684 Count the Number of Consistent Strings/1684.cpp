class Solution {
    vector<bool> valid;

    void updateValid(string allowed){
        valid = vector<bool>(26, false);
        for (int i = 0; i<valid.size(); i++){
            valid[i] = false;
        }
        for (char c: allowed){
            valid[c - 'a'] = true;
        }
    }

    bool isConsistent(string word){
        for (char c: word){
            if (!valid[c - 'a']){
                return false;
            }
        }
        return true;
    }

public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        updateValid(allowed);
        int ans = 0;
        for (string word: words){
            if (isConsistent(word)){
                ans++;
            }
        }
        return ans;
    }
};
