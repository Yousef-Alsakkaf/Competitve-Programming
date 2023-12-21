#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<long long> nCounter(5, 0);
    vector<long long> mCounter(5, 0);

    for(long long i = 1; i <= n; i++)
    {
        nCounter[i % 5]++;
    }
    for(long long i = 1; i <= m; i++)
    {
        mCounter[i % 5]++;
    }

    long long ans = 0;
    ans += nCounter[0] * mCounter[0];
    ans += nCounter[1] * mCounter[4];
    ans += nCounter[2] * mCounter[3];
    ans += nCounter[3] * mCounter[2];
    ans += nCounter[4] * mCounter[1];

    cout << ans << endl; 
}