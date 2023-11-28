#include <iostream>
using namespace std;

int main()
{
    int r, c;
    cin >> r >> c;
    bool isColouful = false;
    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j < c; j++)
        {
            char a;
            cin >> a;
            if(a != 'B' && a != 'W' && a != 'G')
            {
                isColouful = true;
            }
        }
    }
    if(isColouful)
    {
        cout << "#Color";
    }
    else
    {
        cout << "#Black&White";
    }
    return 0;
}