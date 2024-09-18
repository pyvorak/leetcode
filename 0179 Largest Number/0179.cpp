class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> v;
        
        for (const int& num: nums){
            v.push_back(to_string(num));
        }
        
        sort(v.begin(), v.end(), [](const string& a, const string& b){
            return a+b > b+a;
        });

        if (v[0] == "0") return "0";

        string ans;

        for (const string& s: v){
            ans += s;
        }

        return ans;
    }
};
