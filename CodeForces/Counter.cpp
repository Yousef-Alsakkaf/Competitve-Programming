#include <iostream>
using namespace std;

int main()
{
    long long l, r;
    cin >> l >> r;

    if (l % 2 == 1)
        l++;
    if (r - l > 1)
    {
        cout << l << " " << l + 1 << " " << l + 2;
    }
    else
    {
        cout << -1;
    }
    return 0;
}