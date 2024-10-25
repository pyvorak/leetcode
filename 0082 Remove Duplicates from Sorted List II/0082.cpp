class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* start = new ListNode(0, head); 
        ListNode* prev = start;
        ListNode* cur = head;

        while (cur){
            if (cur->next == nullptr || cur->next->val != cur->val){
                prev = cur;
            } else {
                while (cur->next != nullptr && cur->next->val == cur->val) cur = cur->next;
                prev->next = cur->next;
            }
            cur = cur->next;
        }

        return start->next;
    }
};
