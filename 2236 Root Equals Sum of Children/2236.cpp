class Solution {
public:
    bool checkTree(TreeNode* root) {
        return root->left->val + root->right->val == root->val;
    }
};
