class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* lessHead = new ListNode(0);
        ListNode* moreHead = new ListNode(0);
        
        ListNode* less = lessHead;
        ListNode* more = moreHead;
        ListNode* cur = head;

        while (cur){
            if (cur->val < x){
                less->next = cur;
                less = cur;
            } else {
                more->next = cur;
                more = cur;
            }

            cur = cur->next;
        }

        less->next = moreHead->next;
        more->next = nullptr;

        return lessHead->next;
    }
};
