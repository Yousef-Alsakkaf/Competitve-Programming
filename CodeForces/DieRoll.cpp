#include <iostream>
using namespace std;

int main()
{
    int x, y;
    cin >> x >> y;
    string result;
    int maximum = max(x, y);

    switch (maximum)
    {
        case 1: result = "1/1";
        break;
        case 2: result = "5/6";
        break;
        case 3: result = "2/3";
        break;
        case 4: result = "1/2";
        break;
        case 5: result = "1/3";
        break;
        case 6: result = "1/6";
        break;
    }
    cout << result;
    return 0;
}