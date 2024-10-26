class Solution {
public:
    int maxH;
    bool leftFirst;
    int removed[100001];
    
    void dfs(TreeNode* cur, int h){
        if (cur == nullptr) return;

        removed[cur->val] = max(removed[cur->val], maxH);
        maxH = max(maxH, h);

        dfs(leftFirst ? cur->left : cur->right, h+1);
        dfs(leftFirst ? cur->right : cur->left, h+1);
    }

    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        leftFirst = true;
        dfs(root, 0);

        maxH = 0;
        leftFirst = false;
        dfs(root, 0);

        vector<int> ans;

        for (int q: queries) ans.push_back(removed[q]);

        return ans;
    }
};
