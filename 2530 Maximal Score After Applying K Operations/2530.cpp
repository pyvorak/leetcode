class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int> pq;
        
        for (int num: nums){
            pq.push(num);
        }
        
        long long ans = 0;

        while (k--){
            int cur = pq.top(); pq.pop();
            ans += cur;
            pq.push((cur+2)/3);
        }

        return ans;
    }
};
