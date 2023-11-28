#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n, t, k, d;
    cin >> n >> t >> k >> d;
    int t1;
    if(n % k == 0)
    {
        t1 = (n / k) * t;
    }
    else
    {
        t1 = n / k;
        t1 += 1;
        t1 *= t;
    }
    int t2 = t + d;
    if(t2 < t1)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }

    return 0;
}