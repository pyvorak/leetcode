class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> count;
        stringstream ss(s1 + " " + s2);
        string word;
        
        while (ss >> word){
            count[word]++;
        }

        vector<string> ans;

        for (const auto& [word, freq]: count){
            if (freq == 1){
                ans.push_back(word);
            }
        }

        return ans;
    }
};
