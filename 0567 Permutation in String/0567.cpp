class Solution {
public:
    bool valid(vector<int>& a){
        for (int i = 0; i<a.size(); i++){
            if (a[i] != 0){
                return false;
            }
        }
        return true;
    }
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()){
            return false;
        } else {
            vector<int> v(26, 0);

            for (int i = 0; i<s1.size(); i++){
                v[s1[i]-'a']--;
                v[s2[i]-'a']++;
            }

            if (valid(v)){
                return true;
            } else {
                for (int i = s1.size(); i<s2.size(); i++){
                    v[s2[i]-'a']++;
                    v[s2[i-s1.size()]-'a']--;
                    if (valid(v)){
                        return true;
                    }
                }
                return false;
            }
        }
    }
};
