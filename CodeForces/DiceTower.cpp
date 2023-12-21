#include <iostream>
using namespace std;

int main()
{
    int n, z, x, y;
    cin >> n >> z;
    bool isUnique = true;
    for(int i = 0; i < n; i++)
    {
        cin >> x >> y;
        if(x == z || y == z || x == 7 - z || y == 7 - z) isUnique = false;
    }
    if(isUnique) cout << "YES";
    else cout << "NO";
    return 0;
}