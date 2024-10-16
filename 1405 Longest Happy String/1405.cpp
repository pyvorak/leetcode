#define PIC pair<int, char> 
#define PQ priority_queue<PIC> 

class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        PQ pq;

        if (a > 0) pq.push({a, 'a'});
        if (b > 0) pq.push({b, 'b'});
        if (c > 0) pq.push({c, 'c'});

        string ans = "";

        while (!pq.empty()){
            int cnt = pq.top().first;
            char x = pq.top().second;
            pq.pop();
            int n = ans.size();
            if (n >= 2 && ans[n-2] == ans[n-1] && ans[n-1] == x){
                if (pq.empty()){
                    break;
                } else {
                    int cnt2 = pq.top().first;
                    char x2 = pq.top().second;
                    pq.pop();
                    ans += x2;
                    cnt2--;
                    if (cnt2 > 0) pq.push({cnt2, x2}); 
                    pq.push({cnt, x}); 
                }
            } else {
                ans += x;
                cnt--;
                if (cnt > 0) pq.push({cnt, x});
            }
        }

        return ans;
    }
};
