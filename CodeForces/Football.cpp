#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<string, int> map;
    int n, maximum = -1;
    string winningTeam;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        string a;
        cin >> a;
        map[a]++;
        if(map[a] > maximum)
        {
            maximum = map[a];
            winningTeam = a;
        }
    }
    cout << winningTeam;
    return 0;
}