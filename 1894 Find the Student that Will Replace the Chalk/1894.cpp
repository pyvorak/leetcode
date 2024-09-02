class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int total = 0;
        for (int i=0; i<chalk.size(); i++) if ((total += chalk[i]) > k) return i; 
        k %= total;
        for (int i=0; i<chalk.size(); k -= chalk[i++]) if (chalk[i] > k) return i;
        return 0;
    }
};
