class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> ans(m, vector<int>(n, -1));
        ListNode* cur = head;
        int c1 = 0;
        int c2 = n-1;
        int r1 = 0;
        int r2 = m-1;
        
        while (cur && c1 <= c2 && r1 <= r2){
            for (int j = c1; cur && j <= c2; j++){
                ans[r1][j] = cur->val;
                cur = cur->next;
            }

            for (int i = r1+1; cur && i <= r2; i++){
                ans[i][c2] = cur->val;
                cur = cur->next;
            }

            for (int j = c2-1; cur && j >= c1; j--){
                ans[r2][j] = cur->val;
                cur = cur->next;
            }

            for (int i = r2-1; cur && i >= r1+1; i--){
                ans[i][c1] = cur->val;
                cur = cur->next;
            }

            c1++;
            c2--;
            r1++;
            r2--;
        }

        return ans;
    }
};
