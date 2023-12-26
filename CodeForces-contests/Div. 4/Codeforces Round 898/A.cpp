#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int T; 
    cin >> T;
    string result = "";
    while(T--)
    {
        string str;
        cin >> str;

        if(str == "bca" || str == "cab")
        {
            result += "NO\n";
        }
        else
        {
            result += "YES\n";
        }
    }
    cout << result;
    return 0;
}