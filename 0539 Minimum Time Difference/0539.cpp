class Solution {
public:
    int mins(string time){
        int h = stoi(time.substr(0,2));
        int m = stoi(time.substr(3,2));
        return h * 60 + m;
    }

    int findMinDifference(vector<string>& times) {
        sort(times.begin(), times.end());
        int ans = 24 * 60 - mins(times.back()) + mins(times.front());
        for (int i = 1; i < times.size(); i++){
            ans = min(ans, mins(times[i]) - mins(times[i-1]));
        }
        return ans;
    }
};
