class Solution {
public:
    void flipWrite(vector<vector<char>>& ans, int i, int j, char c){
        int x = j;
        int y = ans[0].size() - 1 - i;
        ans[x][y] = c;

    }

    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size();
        int n = box[0].size();

        vector<vector<char>> ans(n, vector<char>(m, '.'));
        char ROCK = '#';
        char WALL = '*';

        for (int i = 0; i < m; i++){
            int bottom = n - 1;
            for (int j = n - 1; j >= 0; j--){
                if (box[i][j] == ROCK){
                    flipWrite(ans, i, bottom--, ROCK);
                } else if (box[i][j] == WALL){
                    flipWrite(ans, i, j, WALL);
                    bottom = j - 1;
                }
            }
        }

        return ans;
    }
};
