class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*> ans(k);
        ListNode* cur = head;
        int n = 0;

        while (cur){
            cur = cur->next;
            n++;
        }

        cur = head;
        int avg = n / k;
        int extra = n % k;

        for (int i = 0; i<k; i++){
            ans[i] = cur;
            int cnt = avg;

            if (extra-- > 0) cnt++;

            while (--cnt && cur) cur = cur->next;

            if (cur) {
                ListNode* prev = cur;
                cur = cur->next;
                prev->next = nullptr;
            }
        }
        return ans;
    }
};
