class Solution {
public:
    TreeNode* build(unordered_map<int, int>& mp, vector<int>& postorder, int l, int r, int& postorderIndex){
        if (l > r) return nullptr;

        int value = postorder[postorderIndex--];
        TreeNode* node = new TreeNode(value);
        int i = mp[value];
        
        node->right = build(mp, postorder, i+1, r, postorderIndex);
        node->left = build(mp, postorder, l, i-1, postorderIndex);

        return node;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int, int> mp;
        int n = inorder.size();

        for (int i = 0; i<n; i++){
            mp[inorder[i]] = i;
        }
        
        int postorderIndex = n-1;
        return build(mp, postorder, 0, n-1, postorderIndex);
    }
};
