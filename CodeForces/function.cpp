#include <iostream>
using namespace std;

int main()
{
    long long exponent;
    cin >> exponent;

    if(exponent % 2 == 0)
    {
        cout << exponent / 2;
    }
    else
    {
        cout << exponent / 2 - exponent;
    }
    return 0;
}