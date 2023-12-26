#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int r1, r2, c1, c2, d1, d2;

    cin >> r1 >> r2 >> c1 >> c2 >> d1 >> d2;
    int x = (d1 -r2 + c1) / 2;
    int c = r2 - c1 + x;
    int b = r2 - c;
    int a = r1 - x;
    if(x == a || x == b || x == c || a == b || a == c || b == c)
    {
        cout << -1;
        return 0;
    }
    if(x < 1 || x > 9 || a < 1 || a > 9 || b < 1 || b > 9 || c < 1 || c > 9)
    {
        cout << -1;
        return 0;
    }
    cout << x << " " << a << endl;
    cout << b << " " << c << endl;
    return 0;
}