class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        vector<vector<int>> pq;
        priority_queue<int, vector<int>, greater<int>> chairs;
        unordered_map<int, int> taken;

        for (int i = 0; i<times.size(); i++){
            chairs.push(i);
            
            int arrive = times[i][0];
            int leave = times[i][1];

            pq.push_back({leave, 0, i});
            pq.push_back({arrive, 1, i});
        }

        sort(pq.begin(), pq.end());

        for (vector<int> cur: pq){
            int take = cur[1], person = cur[2];
            if (take){
                taken[person] = chairs.top(); chairs.pop();
                if (person == targetFriend) return taken[person];
            } else {   
                chairs.push(taken[person]);
            }
        }

        return 0;
    }
};
