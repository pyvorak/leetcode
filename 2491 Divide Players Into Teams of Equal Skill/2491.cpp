class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        int n = skill.size();
        int a = skill[0];
        int b = skill[n-1];
        int total = a + b;
        long long ans = a * b;
        
        for (int i = 1; i < n/2; i++){
            a = skill[i];
            b = skill[n-1-i];
            if (a + b != total){
                return -1;
            } else {
                ans += a*b;
            }
        }

        return ans;
    }
};
