class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        int ans = 0;
        char FREE = '.';
        char WALL = 'W';
        char GUARD = 'G';
        char SEEN = 'X';
        
        vector<vector<char>> grid(m, vector<char>(n, FREE));

        for (auto w: walls){
            grid[w[0]][w[1]] = WALL;
        }

        for (auto g: guards){
            grid[g[0]][g[1]] = GUARD;
        }

        for (auto g: guards){
            vector<int> moves = {-1, 0, 1, 0, -1};

            for (int k = 0; k < moves.size() - 1; k++){
                int di = moves[k];
                int dj = moves[k+1];
                int i = g[0] + di;
                int j = g[1] + dj;
                while (i >= 0 && i < m && j >= 0 && j < n){
                    if (grid[i][j] == WALL || grid[i][j] == GUARD){
                        break;
                    } else {
                        grid[i][j] = SEEN;
                    }
                    i += di;
                    j += dj;
                }
            }
        }

        for (int i = 0; i < m ; i++){
            for (int j = 0; j < n ; j++){
                if (grid[i][j] == FREE){
                    ans++;
                }
            }    
        }

        return ans;
    }
};
