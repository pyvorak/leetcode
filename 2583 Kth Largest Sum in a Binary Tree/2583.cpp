class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        vector<long long> v;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()){
            long long sum = 0;
            queue<TreeNode*> nextQ;

            while (!q.empty()){
                TreeNode* cur = q.front();
                q.pop();

                if (cur->left) nextQ.push(cur->left);
                if (cur->right) nextQ.push(cur->right);

                sum += cur->val;
            }

            v.push_back(sum);
            q = nextQ;
        } 

        if (k <= v.size()){
            sort(v.begin(), v.end(), greater<>());
            return v[k-1];
        } else {
            return -1;
        }
    }
};
