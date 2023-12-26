#include <iostream>
using namespace std;

int main()
{
    string str, str1;
    cin >> str >> str1;

    int left = 0, right = 0;
    int found = false;
    for(int i = 0; i < str.length(); i++)
    {
        if(str[i] == '|') found = true;
        else
        {
            if(found) right++;
            else left++;
        }
    }
    for(int i = 0; i < str1.length(); i++)
    {
        if(left <= right)
        {
            str = str1[i] + str;
            left++;
        }
        else
        {
            str = str + str1[i];
            right++;
        }
    }
    if(left == right) cout << str << endl;
    else cout << "Impossible" << endl;
    return 0;
}