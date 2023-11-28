#include <iostream>
using namespace std;

int main()
{
    long long l, r;
    cin >> l >> r;
    if(l % 2 == 0 && r - l > 1)
    {
        cout << l << " " << l + 1 << " " << l + 2;
    }
    else if(r - l > 2)
    {
        cout << l + 1 << " " << l + 2 << " " << l + 3;
    }
    else
    {
        cout << -1;
    }
    return 0;
}