class Solution {
public:
    bool valid(ListNode* h, TreeNode* p){
        return !h || p && p->val == h->val && (valid(h->next, p->left) || valid(h->next, p->right));
    }

    bool dfs(ListNode* h, TreeNode* p){
        return p && (valid(h, p) or dfs(h, p->left) or dfs(h, p->right));
    }

    bool isSubPath(ListNode* head, TreeNode* root) {
        return dfs(head, root);
    }
};
