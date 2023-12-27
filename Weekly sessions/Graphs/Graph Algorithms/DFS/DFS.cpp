#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// I am assuming that there is no vertex 0 and the starting point is 1

vector<int> dfs(int v, vector<vector<int>> adj)
{
    vector<bool> visited(v+1, false);
    stack<int> s;
    vector<int> dfs; // the result
    
    s.push(1);
    visited[1] = true;
    while(!s.empty())
    {
        int node = s.top();
        s.pop();

        dfs.push_back(node);

        for(int i = 0; i < adj[node].size(); i++)
        {
            int element = adj[node][i];
            if(!visited[element])
            {
                visited[element] = true;
                s.push(element);
            }
        }
    }
    return dfs;
}

int main()
{
    int v, e; // vertices - edges
    cin >> v >> e;

    vector<vector<int>> adj(v + 1);
    for(int i = 0; i < e; i++)
    {
        int u, w;
        cin >> u >> w;

        adj[u].push_back(w);
        adj[w].push_back(u);
    }

    vector<int> dfsResult = dfs(v, adj);
    for (int node : dfsResult) {
        cout << node << " ";
    }

    return 0;
}