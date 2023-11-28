#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int num;
    cin >> num;

    vector<int> programming, math, PE;
    vector<int> team[3];
    for(int i = 0; i < num; i++)
    {
        int a;
        cin >> a;
        if(a == 1)
        {
            programming.push_back(i);
            team[0].push_back(i);
        }
        else if(a == 2)
        {
            math.push_back(i);
            team[1].push_back(i);
        }
        else
        {
            PE.push_back(i);
            team[2].push_back(i);
        }
    }
    int ans = min(min(programming.size(), math.size()), PE.size());
    cout << ans << endl;
    for(int i = 0; i < ans; i++)
    {
        cout << (team[0][i] + 1) << " " << (team[1][i] + 1) << " " << (team[2][i] + 1) << endl;
    }
    return 0;
}