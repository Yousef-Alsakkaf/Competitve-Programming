#include <iostream>
using namespace std;

int main()
{
    string allChars = "qwertyuiopasdfghjkl;zxcvbnm,./";
    string s, d;
    cin >> d >> s;
    for(int i = 0; i < s.length(); i++)
    {
        for(int j = 0; j < allChars.length(); j++)
        {
            if(s[i] == allChars[j] && d == "R")
            {
                cout << allChars[j - 1];
            }
            else if(s[i] == allChars[j] && d == "L")
            {
                cout << allChars[j + 1];
            }
        }
    }
    return 0;
}