class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> mp;

        for (string path: paths){
            istringstream ss(path);
            string folder;
            ss >> folder;

            while (ss){
                string s;
                ss >> s;
                if (s.size() > 0){
                    int i = s.find('(');
                    string filename = s.substr(0, i); 
                    string content = s.substr(i); 
                    mp[content].push_back(folder + "/" + filename);
                }
            }
        }
        
        vector<vector<string>> ans;
        
        for (auto x: mp){
            if (x.second.size() > 1){
                ans.push_back(x.second);
            }
        }
        
        return ans;
    }
};
