#include <iostream>
using namespace std;

int main()
{
    int n, t;
    cin >> n >> t;
    if(t == 10)
    {
        if(n <= 1)
        {
            cout << "-1";
        }
        else{
            n--;
            while(n--)
            {
                cout << 1;
            }
            cout << 0;
        }
    }
    else{
        if(n < 1)
        {
            cout << "-1";
        }
        else{
            while(n--)
            {
                cout << t;
            }
        }
    }
    return 0;
}