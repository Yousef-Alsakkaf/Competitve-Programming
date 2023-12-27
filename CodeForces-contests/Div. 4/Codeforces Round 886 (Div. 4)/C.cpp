#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;

    while(T--)
    {
        string str = "";
        for(int i = 0; i < 8; i++)
        {
            for(int j = 0; j < 8; j++)
            {
                char a;
                cin >> a;
                if(a != '.')
                {
                    str += a;
                }
            }
        }
        cout << str << endl;
    }
    return 0;
}