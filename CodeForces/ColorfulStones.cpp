#include <iostream>
using namespace std;

int main()
{
    string x, y;
    cin >> x >> y;
    int k = 0;
    for(int i = 0; i < y.length(); i++)
    {
        if(x[k] == y[i])
        {
            k++;
        }
    }
    cout << ++k;
    return 0;
}