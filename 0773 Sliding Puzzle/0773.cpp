class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        unordered_set<string> seen;
        queue<string> q;
        vector<int> directions = {-1, 1, 3, -3};
        string startState = "";
        string endState = "123450";
        int moves = 0;
        
        for (auto row: board){
            for (int num: row){
                startState += to_string(num);
            }
        }

        if (startState == endState) return 0;

        q.push(startState);
        seen.insert(startState);

        while (!q.empty()){
            queue<string> nextq;
            moves++;
            while (!q.empty()){
                string curState = q.front(); q.pop();

                int z = curState.find('0');

                for (int dir : directions){
                    int nextCell = z + dir;
                    if (nextCell < 0 || nextCell >= 6 || (z % 3 == 0 && dir == -1) || (z % 3 == 2 && dir == 1)) {
                        continue;
                    }
                    string nextState = curState;
                    swap(nextState[z], nextState[nextCell]);

                    if (seen.find(nextState) == seen.end()){
                        if (nextState == endState) return moves;

                        nextq.push(nextState);
                        seen.insert(nextState);
                    }
                }
            }
            q = nextq;
        }

        return -1;
    }
};
