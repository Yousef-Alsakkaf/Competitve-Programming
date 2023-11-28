#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    string res = "";
    for (int t = 0; t < T; t++)
    {
        int n, k, mn = 1234567, even = 0;
        cin >> n >> k;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            if (x % 2 == 0)
                even++;
            mn = min(mn, x % k == 0 ? 0 : k - (x % k));
            even = min(even, 2);
        }
        if(k == 4) mn = min(mn, 2 - even);
        res += to_string(mn) + "\n";
    }
    cout << res;
}