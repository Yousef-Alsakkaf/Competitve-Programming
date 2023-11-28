#include <iostream>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    while(n > 0)
    {
        for(int i = 0; i < k; i++)
        {
            char c = 'a' + i;
            cout << c;
            n--;
            if(n == 0)
            {
                break;
            }
        }
    }
    return 0;
}