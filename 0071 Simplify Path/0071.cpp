class Solution {
public:
    string simplifyPath(string path) {
        stack<string> stk;
        string w;
        
        for (char c: path + "/"){
            if (c == '/'){
                if (w == ".."){
                    if (!stk.empty()) stk.pop();
                } else if (w != "" && w != "."){
                    stk.push(w);
                }
                w.clear();
            } else {
                w += c;
            }
        }

        string ans = "";

        while (!stk.empty()){
            ans = "/" + stk.top() + ans;
            stk.pop();
        }

        return ans == "" ? "/" : ans;
    }
};
