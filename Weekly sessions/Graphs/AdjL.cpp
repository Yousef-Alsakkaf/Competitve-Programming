#include <iostream>
#include <vector>
using namespace std;

// adjacency list
int main()
{
    int n, m; // vertices - edges
    cin >> n >> m;

    vector<vector<int>> adj(n + 1);

    for(int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    return 0;
}