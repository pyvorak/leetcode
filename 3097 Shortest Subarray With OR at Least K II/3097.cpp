class Solution {
    int BIT_LEN = 32;
public:
    void add(int& num, vector<int>& bits, int& cur){
        for (int i = 0; i < BIT_LEN; i++){
            if (num & 1 << i){
                bits[i]++;
            }
        }
        cur |= num;
    }

    void remove(int& num, vector<int>& bits, int& cur){
        for (int i = 0; i < BIT_LEN; i++){
            int b = 1 << i;
            if (num & b){
                bits[i]--;
                if (bits[i] == 0){
                    cur -= b;
                }
            }
        }
    }

    int minimumSubarrayLength(vector<int>& nums, int k) {
        vector<int> bits(BIT_LEN, 0);
        int l = 0;
        int cur = 0;
        int ans = INT_MAX;

        for (int r = 0; r < nums.size(); r++){
            add(nums[r], bits, cur);

            while (cur >= k && l <= r){
                ans = min(ans, r - l + 1);
                remove(nums[l++], bits, cur);
            }
        }

        return ans == INT_MAX ? -1 : ans;
    }       
};
