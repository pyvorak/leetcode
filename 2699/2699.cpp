# define P pair<int,int>
# define VI vector<int>
# define VP vector<P>
# define V2P vector<VP>
# define PQ priority_queue<P, VP, greater<P>>

class Solution {
    int dijkstra(int a, int b, V2P& adj){
        VI dp(adj.size(), INT_MAX); PQ pq; pq.push({0, a});

        while (!pq.empty()){
            auto [d, u] = pq.top(); pq.pop();
            if (u == b) return d;
            for (auto [v, w]: adj[u]){
                int d2 = d + w;
                if (d2 < dp[v]){
                    dp[v] = d2;
                    pq.push({d2, v});
                }
            }
        }

        return INT_MAX;
    }

public:
    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int a, int b, int t) {
        V2P adj(n, VP()); VI wild;
        
        for (int i = 0; i < edges.size(); i++){
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            if (w > 0) {
                adj[u].push_back({v, w});
                adj[v].push_back({u, w});
            } else {
                wild.push_back(i);
            }
        }

        int d = dijkstra(a, b, adj);
        if (d < t) return {};

        for (int i: wild) edges[i][2] = t+1;
        if (d == t) return edges;

        for (int i: wild){
            int u = edges[i][0], v = edges[i][1];
            edges[i][2] = 1;
            adj[u].push_back({v, 1});
            adj[v].push_back({u, 1});
            int d = dijkstra(a, b, adj);
            if (d <= t){
                edges[i][2] += t - d;
                return edges;
            }
        }

        return {};  
    }
};
