class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* cur = head;

        while (cur && cur->next){
            ListNode* p = new ListNode(gcd(cur->val, cur->next->val));
            p->next = cur->next;
            cur->next = p;
            cur = p->next;
        }

        return head;
    }
};
