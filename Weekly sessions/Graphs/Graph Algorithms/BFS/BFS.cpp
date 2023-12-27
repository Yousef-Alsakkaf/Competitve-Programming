#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> bfs(int v, vector<vector<int>>& adj)
{
    vector<bool> visited(v + 1, false);
    visited[1] = true;
    queue<int> q;
    q.push(1);
    vector<int> bfs; // the result

    while (!q.empty())
    {
        int node = q.front();
        q.pop();

        bfs.push_back(node);
        for (int i = 0; i < adj[node].size(); i++)
        {
            int neighbor = adj[node][i];
            if (!visited[neighbor])
            {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
    return bfs;
}

int main()
{
    int v, e;
    cin >> v >> e;

    vector<vector<int>> adj(v + 1);
    for (int i = 0; i < e; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> result = bfs(v, adj);

    cout << "BFS traversal: ";
    for (int node : result)
    {
        cout << node << " ";
    }

    return 0;
}
