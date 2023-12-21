#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;

    while(T--)
    {
        int degree;
        cin >> degree;
        if(360 % (180 - degree) == 0)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;   
        }
    }
    return 0;
}