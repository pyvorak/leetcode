class Solution {
public:
    void nextState(vector<vector<int>>& board, int x, int y){
        int m = board.size();
        int n = board[0].size();

        int live = 0;

        for (int i = max(x-1, 0); i <= min(x+1, m-1); i++){
            for (int j = max(y-1, 0); j <= min(y+1, n-1); j++){
                if (!(x == i && y == j) && (board[i][j] == 1 || board[i][j] == 3)){
                    live++;
                }
            }
        }

        if (board[x][y] == 1 && live != 2 && live != 3){
            board[x][y] = 3;
        } else if (board[x][y] == 0 && live == 3){
            board[x][y] = 2;
        }
    }

    void cleanUp(vector<vector<int>>& board){
        int m = board.size();
        int n = board[0].size();

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == 2){
                    board[i][j] = 1;
                } else if (board[i][j] == 3){
                    board[i][j] = 0;
                }
            }
        }
    }


    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                nextState(board, i, j);
            }
        }

        cleanUp(board);
    }
};
