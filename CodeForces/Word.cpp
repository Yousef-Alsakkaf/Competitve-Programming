#include <iostream>
using namespace std;
int main()
{
    string s;
    cin >> s;
    int counterS = 0;
    int counterC = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (tolower(s.at(i)) == s.at(i))
        {
            counterS++;
        }
        else
        {
            counterC++;
        }
    }
    string ans;
    if (counterC > counterS)
    {
        for (char c : s)
        {
            ans += toupper(c);
        }
    }
    else if (counterS >= counterC)
    {
        for (char c : s)
        {
            ans += tolower(c);
        }
    }
    cout << ans;
    return 0;
}