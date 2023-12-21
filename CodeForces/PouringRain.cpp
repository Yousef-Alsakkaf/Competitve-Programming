#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    float d, h, v, e;

    cin >> d >> h >> v >> e;

    d = d / 2;
    e = e * M_PI * pow(d, 2);  // Ensure you use a floating-point number for the radius
    if(e >= v)
    {
        cout << "NO" << endl;
    }
    else
    {
        long double time = (M_PI * pow(d, 2) * h) / (v - e);
        cout << "YES" << endl;
        cout <<  (time) << endl;
    }
    return 0;
}
