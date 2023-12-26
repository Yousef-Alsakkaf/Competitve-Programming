#include <iostream>
using namespace std;

int main()
{
    string str;
    cin >> str;

    for(int i = 0; i < str.length(); i++)
    {
        if(str[i] - '0' > 4)
        {
            if(str[i] - '0' == 9 && i == 0)continue;
            str[i] = (9 - (str[i] - '0')) + '0';
        }
    }
    cout << str;
    return 0;
}