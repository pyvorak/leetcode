class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        ListNode *ans = new ListNode(0, head), *prev = ans, *cur = prev->next;
        unordered_set<int> invalid;
        for (int num: nums) invalid.insert(num);
        while (cur != nullptr){
            if (invalid.count(cur->val)) prev->next = cur->next; 
            else prev = prev->next;
            cur = cur->next;
        }
        return ans->next;
    }
};
