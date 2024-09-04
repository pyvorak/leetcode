using namespace std;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int x = 0, y = 0, z = 0, ans = 0;
        set<pair<int, int>> invalid;
        
        for (vector<int> obs: obstacles) invalid.insert({obs[0], obs[1]});

        for (int command: commands){
            if (command < 0) z = (z + (command == -1 ? 1 : 3)) % 4;
            else {
                vector<vector<int>> moves = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
                int dx = moves[z][0], dy = moves[z][1];
                while (command--){
                    x += dx; y += dy;
                    if (invalid.count({x, y})){
                        x -= dx; y -= dy;
                        break;
                    }
                }
                ans = max(ans, (int) (pow(x, 2) + pow(y, 2)));
            }
        }
        
        return ans;
    }
};
