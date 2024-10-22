class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        priority_queue<long long> pq;
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

            pq.push(sum);
            q = nextQ;
        } 

        while (--k && !pq.empty()){
            pq.pop();
        }

        return pq.empty() ? -1 : pq.top();
    }
};
