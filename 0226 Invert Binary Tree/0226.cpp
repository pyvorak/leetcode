class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root){
            TreeNode* leftInverted = invertTree(root->left);
            TreeNode* rightInverted = invertTree(root->right);
            root->left = rightInverted;
            root->right = leftInverted;
        }
        return root;
    }
};
