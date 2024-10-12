class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        priority_queue<int, vector<int>, greater<int>> pq;
        sort(intervals.begin(), intervals.end());

        for (int i = 0; i < intervals.size(); i++){
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (!pq.empty() && pq.top() < start) pq.pop();
            
            pq.push(end);
        }

        return pq.size();
    }
};
