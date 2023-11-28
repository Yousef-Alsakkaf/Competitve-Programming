#include <iostream>
using namespace std;

int main()
{
    long long n;
    cin >> n;
    int pattern [] = {8, 4, 2, 6};
    long long ans;
    if(n != 0)
    {
        ans = pattern[(n - 1) % 4];
    }
    else
    {
        ans = 1;
    }
    cout << ans;
    return 0;
}