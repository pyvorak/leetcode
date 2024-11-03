class Solution {
public:
    bool valid(int i, string s, string goal){
        for (int j = 0 ; j < goal.size(); j++){
            if (s[i] != goal[j]){
                return false;
            }
            i = (i + 1) % s.size();
        }
        return true;
    }

    bool rotateString(string s, string goal) {
        if (s.size() != goal.size()){
            return false;
        } else {
            for (int i = 0; i < s.size(); i++){
                if (valid(i, s, goal)){
                    return true;
                }
            }
            return false;
        }
    }
};
