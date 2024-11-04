class Solution {
public:
    string compressedString(string word) {
        string ans = "";
        
        int n = word.size();

        for (int i = 0; i<n; i++){
            int cnt = 1;
            char c = word[i];

            while (cnt < 9 && i+1 < n && word[i+1] == c){
                i++;
                cnt++;
            } 

            ans += to_string(cnt);
            ans += c;
        }

        return ans;
    }
};
