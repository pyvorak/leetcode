class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*> ans(k, new ListNode(0));
        ListNode* cur = head;
        int n = 0;

        while (cur){
            cur = cur->next;
            n++;
        }

        cur = head;
        int avg = n / k;

        for (int i = 0; i<k; i++){
            ans[i]->next = cur;
            
            int cnt = avg;

            if (cnt * (k-i) < n--) cnt++;

            while (--cnt && cur) {
                cur = cur->next;
                n--;
            }

            if (cur) {
                ListNode* prev = cur;
                cur = cur->next;
                prev->next = nullptr;
            }

            ans[i] = ans[i]->next;
        }
        return ans;
    }
};
