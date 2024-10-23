#define P pair<int, int>
#define PQ priority_queue<P, vector<P>, greater<P>>
class Solution {
public:
    int getSquareValue(vector<vector<int>>& board, int position){
        int n = board.size();
        
        int rowFromBottom = (position - 1) / n; 
        int row = n - 1 - rowFromBottom;
        
        int colFromLeft = (position - 1) % n;
        int col = rowFromBottom % 2 == 0 ? colFromLeft : n - 1 - colFromLeft;

        return board[row][col] == -1 ? position : board[row][col];
    }

    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        vector<bool> seen(n*n+1, false);

        PQ pq;
        pq.push({0,1});

        while (!pq.empty()){
            int moves = pq.top().first;
            int position = pq.top().second;
            pq.pop();

            if (position == n*n) return moves;

            for (int nextPosition = position+1; nextPosition <= min(position + 6, n*n); nextPosition++){
                int nextSquare = getSquareValue(board, nextPosition);

                if (!seen[nextSquare]){
                    seen[nextSquare] = true;
                    pq.push({moves+1, nextSquare});
                }
            }
        }

        return -1;
    }
};
