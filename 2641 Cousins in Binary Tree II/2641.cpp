#define P pair<TreeNode*, long long>

class Solution {
public:
    TreeNode* replaceValueInTree(TreeNode* root) {
        vector<P> v = {{new TreeNode(0, root, nullptr), 0}};

        while (!v.empty()){
            long long sum = 0;

            for (P& cur: v){
                long long curSum = 0;
                TreeNode* parent = cur.first;    

                for (TreeNode* child : {parent->left, parent->right}){
                    if (child) curSum += child->val;
                }
                
                cur = {parent, curSum};        
                sum += curSum;
            }

            vector<pair<TreeNode*, long long>> nextV;

            for (P& cur: v){
                long long newVal = sum - cur.second;
                TreeNode* parent = cur.first;    

                for (TreeNode* child : {parent->left, parent->right}){
                    if (child) {
                        child->val = newVal;
                        nextV.push_back({child, 0});
                    }
                }
            }

            v = nextV;
        }

        return root;
    }
};
