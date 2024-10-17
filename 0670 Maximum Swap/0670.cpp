class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        int n = s.size();
        vector<int> last(10, -1);

        for (int i = 0; i < n; i++) last[s[i] - '0'] = i;

        for (int i = 0; i < n; i++){
            for (int x = 9; x > s[i] - '0'; x--){
                int j = last[x];
                if (j > i){
                    swap(s[i], s[j]);
                    return stoi(s);
                }
            }
        }

        return num;
    }
};

