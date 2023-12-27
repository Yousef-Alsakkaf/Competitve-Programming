#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m; // vertices - edges
    cin >> n >> m;

    vector<pair<int, int>> edgeLists(m);
    
    for(int i = 0; i < m; i++)
    {
        int u, v; 
        cin >> u >> v;

        edgeLists[i].first = u;
        edgeLists[i].second = v;
    }

    // check
    for(int i = 0; i < m; i++)
    {
        cout << "edge " << i + 1 << ": " << edgeLists[i].first << " " << edgeLists[i].second << endl;
    }
}