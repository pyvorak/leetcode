class Solution {
public:
    bool isCircularSentence(string sentence) {
        int n = sentence.size();

        if (sentence[0] != sentence[n-1]){
            return false;
        } else {
            for (int i = 1; i < n-1; i++){
                if (sentence[i] == ' ' && sentence[i-1] != sentence[i+1]){
                    return false;
                }
            }
            return true;   
        }
    }
};
