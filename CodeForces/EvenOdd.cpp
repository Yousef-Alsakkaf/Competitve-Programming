#include <iostream>
using namespace std;

int main()
{
    long long n, k;
    cin >> n >> k;
    if(n % 2 == 0) n /= 2;
    else n = n / 2 + 1;

    if(k <= n) k = k * 2 - 1;
    else{
        k -= n;
        k *= 2;
    }

    cout << k;
    return 0;
}