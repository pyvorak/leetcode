class Solution {
public:
    void inorder(TreeNode* cur, vector<int>& v){
        if (cur->left) inorder(cur->left, v);
        v.push_back(cur->val);
        if (cur->right) inorder(cur->right, v);
    }

    int getMinimumDifference(TreeNode* root) {
        vector<int> v;
        inorder(root, v);
        
        int ans = INT_MAX;

        for (int i = 1; i < v.size(); i++){
            ans = min(ans, v[i] - v[i-1]);
        }

        return ans;
    }
};
